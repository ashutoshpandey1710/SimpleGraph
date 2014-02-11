import re
from pprint import pprint
from graphutils import Vertex, Queue

class Graph:
	def __init__(self, directed=True):
		self.edges = {}
		self.vertex_id_to_object = {}
		self.dfs_time = 0
		self.directed = directed
		# self.count = 0
	
	def insertEdge(self, v1, v2):
		if not self.vertex_id_to_object.has_key(v1):
			self.vertex_id_to_object[v1] = Vertex(v1)
		if not self.vertex_id_to_object.has_key(v2):
			self.vertex_id_to_object[v2] = Vertex(v2)
		# self.edges[v1] = append(v2)
		if self.edges.has_key(v1):
			self.edges[v1].append(v2)
			if not self.directed:
				if self.edges.has_key(v2):
					self.edges[v2].append(v1)
				else:
					self.edges[v2] = [v1]
			else:
				self.edges[v2] = []
		else:
			# print self.edges
			self.edges[v1] = [v2]
		# print self.edges['gandalf']
		
	def readFile(self, filename):
		lines = open(filename, 'r').read().split('\r\n')
		# print lines
		for line in lines:
			words = re.split('\t', line)
			# print words
			self.insertEdge(words[0], words[1])

	def dfs_visit(self, start):
		#actual recursive dfs
		self.dfs_time += 1
		print "Currently at ", start
		current = self.vertex_id_to_object[start]
		current.setColor('gray')
		current.setInTime(self.dfs_time)
		for dest in self.edges.get(start, []):
			dest = self.vertex_id_to_object[dest]
			if dest.getColor() == 'white':
				dest.setDfsParent(current)
				self.dfs_visit(dest.getId())
		self.dfs_time += 1
		current.setColor('black')
		current.setOutTime(self.dfs_time)
		
		

	def dfs_trees(self):
		#dfs forest construction
		self.dfs_time = 0
		for object in self.vertex_id_to_object.values():
			object.setColor('white')
			object.setDfsParent(None)
			object.setInTime(-1)
			object.setOutTime(-1)
		for id, object in self.vertex_id_to_object.items():
			if object.getColor() == 'white':	
				self.dfs_visit(id)

if __name__ == '__main__':
	g = Graph()
	# g.insertEdge('a', 'b')
	g.readFile('testfile.txt')
	g.dfs_trees()
	pprint(g.edges)
	# pprint(g.edges)