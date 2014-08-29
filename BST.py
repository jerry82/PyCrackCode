'''
	implementation of Tree data-structure
'''

class BSTNode:
	def __init__(self, value):
		self.__value = value
		self.__left = None
		self.__right = None
		self.__parent = None

	@property 
	def value(self):
		return self.__value

	@value.setter
	def value(self, v):
		self.__value = v

	@property 
	def left(self):
		return self.__left

	@left.setter
	def left(self, node):
		self.__left = node

	@property
	def right(self):
		return self.__right

	@right.setter
	def right(self, node):
		self.__right = node

	@property 
	def parent(self):
		return self.__parent

	@parent.setter
	def parent(self, node):
		self.__parent = node

class BST:
	def __init__(self):
		self.__root = None
		self.__count = 0

	@property 
	def count(self):
		return self.__count

	@property 
	def root(self):
		return self.__root

	def add(self, value):
		if (self.__count == 0):
			self.__root = BSTNode(value)
			self.__count = 1
			return

		cur = self.__root

		while (True):
			if value > cur.value:
				if cur.right == None:
					cur.right = BSTNode(value)
					cur.right.parent = cur
					break
				else:
					cur = cur.right

			elif value < cur.value:
				if cur.left == None:
					cur.left = BSTNode(value)
					cur.left.parent = cur
					break
				else:
					cur = cur.left

		self.__count += 1

	#display
	def inOrder(self, node):
		if (node == None):
			return

		self.inOrder(node.left)
		print(node.value, end=" ")
		self.inOrder(node.right)

	def preOrder(self, node):	
		if (node == None):
			return
		
		print(node.value, end=" ")
		self.inOrder(node.left)
		self.inOrder(node.right)

	def postOrder(self, node):
		if (node == None):
			return

		self.inOrder(node.left)
		self.inOrder(node.right)
		print(node.value, end=" ")

	#bread first search
	def levelOrder(self):
		queue = [] 
		queue.append(self.__root)

		while len(queue) > 0:
			cur = queue.pop(0)
			print(cur.value, end=" ")

			if (cur.left is not None):
				queue.append(cur.left)
			if (cur.right is not None):
				queue.append(cur.right)


'''test'''
'''
test = BST()
arr = [30, 20, 40, 10, 37, 45, 12]

for n in arr:
	test.add(n)
test.inOrder(test.root)
print()
test.preOrder(test.root)
print()
test.postOrder(test.root)
print()
test.levelOrder()
'''

