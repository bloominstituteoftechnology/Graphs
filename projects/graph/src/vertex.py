class Vertex:
	def __init__(self, vertex_id):
		self.vertex_id = vertex_id
		self.edges = set()
	def __repr__(self):
		return f'{self.edges}'