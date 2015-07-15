#!/usr/bin/env python

from addr import *
import socket, os

class Nanonet(object):
	def __init__(self, topo, linknet, loopnet):
		self.topo = topo
		self.linknet = linknet
		self.loopnet = loopnet

	def assign(self):
		for e in self.topo.edges:
			enet = self.linknet.next_net()
			a1 = enet[:]
			a2 = enet[:]
			a1[-1] = 1
			a2[-1] = 2

			e.node1.intfs_addr[e.port1] = socket.inet_ntop(socket.AF_INET6, str(a1))+'/'+str(self.linknet.submask)
			e.node2.intfs_addr[e.port2] = socket.inet_ntop(socket.AF_INET6, str(a2))+'/'+str(self.linknet.submask)

		for n in self.topo.nodes:
			enet = self.loopnet.next_net()
			enet[-1] = 1

			n.addr = socket.inet_ntop(socket.AF_INET6, str(enet))+'/'+str(self.loopnet.submask)

	def start(self):
		self.topo.build()
		self.assign()

		for n in self.topo.nodes:
			dist, path = self.topo.dijkstra(n)
			for t in dist.keys():
				if len(path[t]) == 0:
					continue
				e = self.topo.get_minimal_edge(n, path[t][0])
				tmp = e.port1 if e.node1 == path[t][0] else e.port2
				n.routes[t] = (path[t][0].intfs_addr[tmp].split("/")[0], dist[t])

		for n in self.topo.nodes:
			print('ip netns add %s' % n.name)
			print('ip netns exec %s ifconfig lo up' % n.name)
			print('ip netns exec %s ip -6 ad ad %s dev lo' % (n.name, n.addr))
			print('ip netns exec %s sysctl net.ipv6.conf.all.forwarding=1' % n.name)
#			print('ip netns exec %s sysctl net.ipv4.conf.all.rp_filter=0' % n.name)

		for e in self.topo.edges:
			dev1 = '%s-eth%d' % (e.node1.name, e.port1)
			dev2 = '%s-eth%d' % (e.node2.name, e.port2)

			print('ip link add name %s type veth peer name %s' % (dev1, dev2))
			print('ip link set %s netns %s' % (dev1, e.node1.name))
			print('ip link set %s netns %s' % (dev2, e.node2.name))
			print('ip netns exec %s ifconfig %s add %s up' % (e.node1.name, dev1, e.node1.intfs_addr[e.port1]))
			print('ip netns exec %s ifconfig %s add %s up' % (e.node2.name, dev2, e.node2.intfs_addr[e.port2]))

		for n in self.topo.nodes:
			for r in n.routes.keys():
				nh, metric = n.routes[r]
				print('ip netns exec %s ip -6 ro ad %s via %s metric %d' % (n.name, r.addr, nh, metric))
