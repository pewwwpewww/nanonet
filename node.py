#!/usr/bin/env python

class Node(object):
	def __init__(self, name):
		self.name = name
		self.cur_intf = 0
		self.intfs = []
		self.intfs_addr = {}
		self.addr = None

		self.routes = {}

	def add_intf(self, intf):
		self.intfs.append(intf)

	def new_intf(self):
		i = self.cur_intf
		self.cur_intf += 1
		return i

class Edge(object):
	def __init__(self, node1, node2, port1, port2, cost):
		self.node1 = node1
		self.node2 = node2
		self.port1 = port1
		self.port2 = port2
		self.cost = cost

class Topo(object):
	def __init__(self):
		self.nodes = set()
		self.edges = list()

	def build(self):
		pass

	def add_node(self, name):
		n = Node(name)
		self.nodes.add(n)
		return n

	def get_node(self, name):
		for n in self.nodes:
			if n.name == name:
				return n

		return None

	def add_link(self, node1, node2, port1=None, port2=None, cost=1):
		if port1 is None:
			port1 = node1.new_intf()
		if port2 is None:
			port2 = node2.new_intf()

		node1.add_intf(port1)
		node2.add_intf(port2)

		e = Edge(node1, node2, port1, port2, cost)
		self.edges.append(e)
		return e

	def get_edges(self, node1, node2):
		res = []

		for e in self.edges:
			if e.node1 == node1 and e.node2 == node2 or e.node1 == node2 and e.node2 == node1:
				res.append(e)

		return res

	def get_minimal_edge(self, node1, node2):
		edges = self.get_edges(node1, node2)
		cost = 2**32
		res = None

		for e in edges:
			if e.cost < cost:
				cost = e.cost
				res = e

		return res

	def get_neighbors(self, node1):
		res = set()

		for e in self.edges:
			if e.node1 == node1:
				res.add(e.node2)
			elif e.node2 == node1:
				res.add(e.node1)

		return res

	def dijkstra(self, src):
		dist = {}
		prev = {}
		path = {}
		Q = set()

		dist[src] = 0
		prev[src] = None

		for v in self.nodes:
			if v != src:
				dist[v] = 2**32
				prev[v] = None
				path[v] = None
			Q.add(v)

		while len(Q) > 0:
			u = None
			tmpcost = 2**32
			for v in Q:
				if dist[v] < tmpcost:
					tmpcost = dist[v]
					u = v

			S = []
			w = u
			while prev[w] is not None:
				S.append(w)
				w = prev[w]
			path[u] = list(reversed(S))

			Q.remove(u)

			neighs = self.get_neighbors(u)
			for v in neighs:
				if v not in Q:
					continue
				alt = dist[u] + self.get_minimal_edge(u, v).cost
				if alt < dist[v]:
					dist[v] = alt
					prev[v] = u

		return dist, path
