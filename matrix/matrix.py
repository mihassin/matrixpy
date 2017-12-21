from random import random

class Matrix:

	def __init__(self, data):
		try:
			if not isinstance(data, list) or not isinstance(data[0], list):
				raise AttributeError("Illegal attribute type.")
		except IndexError:
			raise RuntimeError("Illegal matrix dimensions.")
		N = len(data[0])
		for i, row in enumerate(data[1:]):
			if not len(row) == N:
				raise IndexError("Rows " + str(0) + " and " + str(i) + " do not have same length.")
		self.data = data
		self.M = len(data)
		self.N = len(data[0])

	@staticmethod
	def random(M, N):
		return Matrix([[random() for j in range(N)] for i in range(M)])

	@staticmethod
	def identity(N):
		return Matrix([[0**abs(j-i) for j in range(N)] for i in range(N)])

	def __eq__(self, other):
		if not self.M == other.M or not self.N == other.N:
			raise RuntimeError("Illegal matrix dimensions.")
		for r1, r2 in zip(self.data, other.data):
			for v1, v2 in zip(r1, r2):
				if not v1 == v2:
					return False
		return True

	def __add__(self, other):
		if not self.M == other.M or not self.N == other.N:
			raise RuntimeError("Illegal matrix dimensions.")
		return Matrix([[v1 + v2 for v1, v2 in zip(r1, r2)] for r1, r2 in zip(self.data, other.data)])

	def __sub__(self, other):
		if not self.M == other.M or not self.N == other.N:
			raise RuntimeError("Illegal matrix dimensions.")
		return self + (other * -1)

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Matrix([[other*value for value in row] for row in self.data])
		elif isinstance(other, Matrix):
			if not self.N == other.M:
				raise RuntimeError("Illegal matrix dimensions.")
			return "TODO"
		else:
			raise TypeError("Illegal types.")

	def __rmul__(self, other):
		return self * other

	def __neg__(self):
		return self * -1

	def size(self):
		return self.M, self.N

	def transpose(self):
		return Matrix([[self.data[i][j] for i in range(self.M)] for j in range(self.N)])

	def issquare(self):
		return self.N == self.M

	def isidentity(self):
		if not self.issquare():
			return RuntimeError("Not a square matrix.")
		for i in range(self.M):
			for j in range(self.N):
				value = 1 if i == j else 0
				if not data[i][j] == value:
						return False
		return True

	def diagonal(self):
		if not self.issquare():
			return RuntimeError("Not a square matrix.")
		return [self.data[i][i] for i in range(self.M)]

	def show(self):
		for row in self.data:
			print(*row)