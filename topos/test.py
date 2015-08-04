#!/usr/bin/env python

from node import *
from net import *

class TestTopo(Topo):
	def build(self):
		seat = self.add_node("seat")
		losa = self.add_node("losa")
		salt = self.add_node("salt")
		hous = self.add_node("hous")
		kans = self.add_node("kans")
		chic = self.add_node("chic")
		atla = self.add_node("atla")
		wash = self.add_node("wash")
		newy = self.add_node("newy")

		self.set_default_delay(3, 5)

		self.add_link(seat, salt, 0, 3, cost=913) # 913
		self.add_link(seat, losa, 1, 2, cost=1342) # 1342
		self.add_link(losa, salt, 0, 2, cost=1303) # 1303
		self.add_link(salt, kans, 0, 4, cost=1329) # 1329
		self.add_link(salt, kans, 1, 3, cost=1330) # 1330
		self.add_link(losa, hous, 1, 1, cost=1705) # 1705
		self.add_link(hous, kans, 2, 2, cost=818) # 818
		self.add_link(kans, chic, 0, 4, cost=690) # 690
		self.add_link(kans, chic, 1, 3, cost=689) # 689
		self.add_link(atla, wash, 0, 2, cost=700) # 700
		self.add_link(atla, wash, 1, 1, cost=699) # 699
		self.add_link(atla, hous, 2, 0, cost=1385) # 1385
		self.add_link(atla, chic, 3, 2, cost=1045) # 1045
		self.add_link(wash, chic, 3, 1, cost=905) # 905
		self.add_link(wash, newy, 0, 0, cost=277) # 277
		self.add_link(wash, newy, 4, 1, cost=278) # 278
		self.add_link(chic, newy, 0, 2, cost=1000) # 1000

topo = TestTopo()

#net = Nanonet(topo, V6Net('fc00:1::', 32, 64), V6Net('fc00:2::', 32, 64))
#net = Nanonet(topo)
#net.start()
net = Nanonet.load('nano.net')
#net.dump_commands()

t, edge, rm_routes, chg_routes = net.igp_prepare_link_down("salt", "seat")
net.apply_topo(t)
net.igp_apply_link_down(edge, rm_routes, chg_routes)

#debug=True
#if debug:
#	dist, path = topo.dijkstra(topo.get_node("seat"))

#	for n in dist.keys():
#		print "seat - %s: %d" % (n.name, dist[n])
#		print map(lambda x: x.name, path[n])
#		print

#	for e in topo.edges:
#		print '%s[%d] - %s[%d]: %s - %s' % (e.node1.name, e.port1, e.node2.name, e.port2, e.node1.intfs_addr[e.port1], e.node2.intfs_addr[e.port2])

#	print

for n in net.topo.nodes:
	print '# %s loop: %s' % (n.name, n.addr)
