class Queue:

	def __init__(self):
		self.q = []
		self.size = 0
		
	def push(self, item):
		self.q = ([item] + self.q)
		self.size += 1

	def empty(self):
		return (len(self.q) <= 0)
		

	def pop(self):
		if self.empty():
			print "Queue.pop(): Queue is empty!!"
			return ''
		else:
			e = self.q.pop()
			self.size -= 1
			return e

class Vertex:
	def __init__(self, id, color='white'):
		self.id = id
		self.intime = -1        
		self.outtime = -1
		self.color = color
		self.dfs_parent = None
	
	def __str__(self):
		return str(self.id)
	
	#Getters and setters
	def getInTime(self): return self.intime
	def setInTime(self, time): self.intime = time
	
	def getOutTime(self): return self.outtime
	def setOutTime(self, time): self.outtime = time
	
	def getId(self): return self.id
	def setId(self, id): self.id = id
	
	def getColor(self): return self.color
	def setColor(self, color): self.color = color
	
	def getDfsParent(self): return self.dfs_parent
	def setDfsParent(self, dfs_parent): self.dfs_parent = dfs_parent