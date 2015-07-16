#!/usr/bin/env python

from addr import *
import socket, os

class Nanonet(object):
	def __init__(self, topo, linknet=None, loopnet=None):
		self.topo = topo

		if linknet is None:
			linknet = V6Net('fc00:42::', 32, 64)

		if loopnet is None:
			loopnet = V6Net('fc00:2::', 32, 64)

		self.linknet = linknet
		self.loopnet = loopnet

	def assign(self):
		for e in self.topo.edges:
			enet = self.linknet.next_net()
			a1 = enet[:]
			a2 = enet[:]
			a1[-1] = 1
			a2[-1] = 2

#			print 'Assigning %s - %s' % (socket.inet_ntop(socket.AF_INET6, str(a1)), socket.inet_ntop(socket.AF_INET6, str(a2)))
#			print 'With submask %d' % self.linknet.submask
#			print e.port1
#			print e.port2
#			print 'For port1 %d and port2 %d' % (e.port1, e.port2)

			e.node1.intfs_addr[e.port1] = socket.inet_ntop(socket.AF_INET6, str(a1))+'/'+str(self.linknet.submask)
			e.node2.intfs_addr[e.port2] = socket.inet_ntop(socket.AF_INET6, str(a2))+'/'+str(self.linknet.submask)

		for n in self.topo.nodes:
			enet = self.loopnet.next_net()
			enet[-1] = 1

			n.addr = socket.inet_ntop(socket.AF_INET6, str(enet))+'/'+str(self.loopnet.submask)

	def start(self):
		print '# Building topology...'
		self.topo.build()
		print '# Assigning prefixes...'
		self.assign()

		print '# Running dijkstra... (%d nodes)' % len(self.topo.nodes)
		cnt = 0
		for n in self.topo.nodes:
			print '# Running dijkstra for node %s (%d/%d)' % (n.name, cnt, len(self.topo.nodes))
			dist, path = self.topo.dijkstra(n)
			for t in dist.keys():
				if len(path[t]) == 0:
					continue
				e = self.topo.get_minimal_edge(n, path[t][0])
				tmp = e.port1 if e.node1 == path[t][0] else e.port2
				n.routes[t] = (path[t][0].intfs_addr[tmp].split("/")[0], dist[t])
			cnt += 1

		host_cmd = []
		node_cmd = {}

		for n in self.topo.nodes:
			host_cmd.append('ip netns add %s' % n.name)
			node_cmd[n] = []
			node_cmd[n].append('ifconfig lo up')
			node_cmd[n].append('ip -6 ad ad %s dev lo' % n.addr)
			node_cmd[n].append('sysctl net.ipv6.conf.all.forwarding=1')

		for e in self.topo.edges:
			dev1 = '%s-%d' % (e.node1.name, e.port1)
			dev2 = '%s-%d' % (e.node2.name, e.port2)

			host_cmd.append('ip link add name %s type veth peer name %s' % (dev1, dev2))
			host_cmd.append('ip link set %s netns %s' % (dev1, e.node1.name))
			host_cmd.append('ip link set %s netns %s' % (dev2, e.node2.name))
			node_cmd[e.node1].append('ifconfig %s add %s up' % (dev1, e.node1.intfs_addr[e.port1]))
			node_cmd[e.node2].append('ifconfig %s add %s up' % (dev2, e.node2.intfs_addr[e.port2]))

		for n in self.topo.nodes:
			for r in n.routes.keys():
				nh, metric = n.routes[r]
				node_cmd[n].append('ip -6 ro ad %s via %s metric %d' % (r.addr, nh, metric))

		for c in host_cmd:
			print c

		for n in node_cmd.keys():
			print('ip netns exec %s bash -c \'%s\'' % (n.name, "; ".join(node_cmd[n])))
