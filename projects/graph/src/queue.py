class Queue:
	def __init__(self):
		self.size = 0
		self.storage = []

	def enqueue(self, item):
		# add to tail
		self.storage.append(item)
		self.size += 1

	def dequeue(self):
		# remove from head
		if self.size:
			self.size -= 1
		return self.storage.pop(0)

	def len(self):
		return self.size
