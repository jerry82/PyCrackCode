class Node:
	def __init__(self, value):
		self.__left = None
		self.__right = None
		self.__mom = None
		self.__value = value
		self.__dir = ''

	@property 
	def value(self):
		return self.__value

	@value.setter
	def value(self, value):
		self.__value = value

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
	def mom(self):
		return self.__mom

	@mom.setter
	def mom(self, value):
		self.__mom = value

	@property 
	def dir(self):
		return self.__dir

	@dir.setter
	def dir(self, value):
		self.__dir = value

class GNode:
	def __init__(self):
		self.__node = ''
		self.__neighbors = []

	@property 
	def node(self):
		return self.__node

	@node.setter
	def node(self, value):
		self.__node = value

	@property 
	def neighbors(self):
		return self.__neighbors

	@neighbors.setter
	def neighbors(self, value): 
		self.__neighbors = value

	def addNB(self, nodeName):
		if nodeName == self.__node:
			return

		if (nodeName not in self.__neighbors):
			self.__neighbors.append(nodeName)

class Graph:
	def __init__(self):
		self.__dict = {}

	def addEdge(self, edge, twoWay):
		if (len(edge) !=2):
			print('edge is invalid')

		tmp = list(edge)

		k = edge[0]
		v = edge[1]
		self.add(k, v)

		if (twoWay):
			self.add(v, k)

	#helper
	def add(self, k, v):
		if (k not in self.__dict):
			self.__dict[k] = []

		if (v not in self.__dict):
			self.__dict[v] = []

		if k in self.__dict:
			if v not in self.__dict[k]:
				self.__dict[k].append(v)


	def show(self):
		for k in self.__dict:
			print(k)
			print(list(self.__dict[k]));


	def dfs(self, start):
		visited = []
		stack = []

		stack.append(start)
		visited.append(start)

		while len(stack) > 0:
			cur = stack[-1]

			neighbors = self.__dict[cur]
			next = None
			for n in neighbors:
				if n not in visited:
					next = n
					break

			if next is not None:
				stack.append(next)
				visited.append(next)
			else:
				stack.pop()

		print(visited)


	def bfs(self, start):
		visited = []
		queue = []

		visited.append(start)
		queue.append(start)

		while len(queue) > 0:
			cur = queue[0]

			neighbors = self.__dict[cur]
			for n in neighbors:
				if n not in visited:
					queue.append(n)
					visited.append(n)

			queue.pop(0)

		print(visited)


	def findRoute(self, start, end):

		visited = [] 
		queue = [] 

		visited.append(start)
		queue.append(start)

		while (len(queue) > 0): 
			cur = queue[0]

			neighbors = self.__dict[cur]
			for n in neighbors:
				if n == end:
					return True
				if n not in visited:
					queue.append(n)
					visited.append(n)


			queue.pop(0)

		print(visited)

		return False

class Tree:
	def __init__(self):
		self.__root = None

	@property 
	def root(self):
		return self.__root

	@root.setter
	def root(self, value):
		self.__root = value

	def find(self, value):
		node = None

		if self.__root.value == value:
			return self.__root

		cur = self.__root
		while (cur is not None):
			if value > cur.value:
				cur = cur.right
			elif value < cur.value:
				cur = cur.left
			else:
				node = cur
				break

		return node

	def add(self, value):
		if (self.__root is None):
			self.__root = Node(value)
		else:

			cur = self.__root
			while (cur is not None):
				#right
				if (cur.value <= value):
					if (cur.right is not None):
						cur = cur.right
					else:
						cur.right = Node(value)
						cur.right.dir = 'r'
						cur.right.mom = cur
						break;
				#left
				elif (cur.value > value):
					if (cur.left is not None):
						cur = cur.left
					else:
						cur.left = Node(value)
						cur.left.dir = 'l'
						cur.left.mom = cur
						break

	def remove(self, value):

		isLeft = True
		
		if self.__root.value == value:
			self.__root = None

		cur = self.__root
		momNode = None

		while (cur is not None):
			#if find 
			if (cur.value == value):
				break

			#if not find 
			momNode = cur
			if value > cur.value:
				cur = cur.right
				isLeft = False
			else:
				cur = cur.left
				isLeft = True



		#if found
		if (cur is not None):
			#print('found:', cur.value, ' has mom: ', momNode.value, 'is left: ', isLeft)
			#is leave
			if (cur.left is None and cur.right is None):
				if (isLeft):
					momNode.left = None
				else:
					momNode.right = None

			#has 2 children
			elif cur.left is not None and cur.right is not None:
				
				#find left most of right child
				tmp = cur.right
				prev = cur
				while (tmp.left is not None):
					prev = tmp 
					tmp = tmp.left

				#print('found left most: ', tmp.value, 'cur: ', cur.value)
				
				#swap value with cur
				cur.value = tmp.value
				#remove tmp
				if (tmp.right is not None):
					prev.left = tmp.right
				else:
					prev.left = None

			#has 1 child
			else:
				if (isLeft):
					momNode.left = cur.left if (cur.left is not None) else cur.right
				else:
					momNode.right = cur.left if (cur.left is not None) else cur.right

	def inOrder(self, node):
		if (node is None):
			return

		self.inOrder(node.left)

		if (node.mom is None):
			print(node.value, end=' ')
		else:
			print(node.value, '-', node.mom.value)
		self.inOrder(node.right)

	def preOrder(self, node):
		if (node is None):
			return

		print(node.value, end=' ')
		self.preOrder(node.left)
		self.preOrder(node.right)

	def postOrder(self, node):
		if (node is None):
			return

		self.postOrder(node.left)
		self.postOrder(node.right)
		print(node.value, end=' ')



class Chapter4:
	def __init__(self):
		pass

	#check for balance tree
	#table should only return <= 2 elements for the tree to be considered balanced
	def Solve41(self, node, depth, table):
		if (node is None):
			return

		if (node.left is None and node.right is None):
			print('leave: ', node.value, 'depth:' , depth)
			if (len(table) == 0):
				table.append(depth)
			else:
				if abs(table[0] - depth) == 1 and depth not in table:
					table.append(depth)
			return

		depth += 1
		self.Solve41(node.left, depth, table)
		self.Solve41(node.right, depth, table)

	def Solve42(self):
		graph = Graph()
		twoWay = False
		edges = ['AB','AG','AD','BF','BE','EG','FD','FC','CH']

		for e in edges:
			graph.addEdge(e, twoWay)

		found = graph.findRoute('A', 'H')
		if (found):
			print('there is a route')
		else:
			print('route not found')

	#to build a shorted height tree, apply recursive alg, start from middle
	#left arr will be left branch and right arr will be right branch
	def Solve43(self, arr, tree, start, end):
		mid = int((start + end) / 2)
		tree.add(arr[mid])

		if (start <= mid - 1):
			self.Solve43(arr, tree, start, mid - 1)
		if (end >= mid + 1):
			self.Solve43(arr, tree, mid + 1, end)	


	#create link lists
	def Solve44(self):
		arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
		tree = Tree()
		for n in arr:
			tree.add(n)

		lists = []

		while True:

			l = len(lists)
			if (l == 0):
				tmp = []
				tmp.append(tree.root)
				lists.append(tmp)
				continue

			tmp = lists[l - 1]
			noChild = True
			newTmp = []
			for node in tmp:
				if node.left is not None:
					newTmp.append(node.left)
					noChild = False
				if node.right is not None:
					newTmp.append(node.right)
					noChild = False 

			lists.append(newTmp)

			if noChild:
				break

		for li in lists:
			self.showValue(li)

	def Solve45(self, value):
		arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
		tree = Tree()
		for i in arr:
			tree.add(i)

		v = value
		#find node with value = 4
		node = None

		cur = tree.root
		while (node is None): 

			if (cur == None):
				return

			if (cur.value == v):
				node = cur
			else:
				if (v > cur.value):
					cur = cur.right
				else:
					cur = cur.left


		#find next node (right)
		next = None
		if (node == None):
			print('node does not exist')
		else:
			'''
			if (node.mom is not None):
				print('found node with mom: ', node.mom.value)
			'''

			#if has right child then return most left of right child
			if (node.right is not None):
				if (node.right.left is not None):
					next = node.right.left
				else:
					next = node.right
			else:
				#root has not right node
				if node.mom is None:
					next = None
				else:
					#if is left child then return mom (node has no right child)
					if node.dir == 'l':
						next = node.mom

					elif node.dir == 'r':
						#if is right child and mom is left child, return mom of mom, if mom is right child 
						#move up to the next level
						cur = node.mom
						while (cur.mom is not None):
							if (cur.mom.right.value == cur.value):
								cur = cur.mom
							else:
								break

						if (cur.mom is not None):
							next = cur.mom

		if (next is not None):
			print('cur: ', node.value, ' next: ', next.value)
		else:
			print('cur: ', node.value, ' next: None')

	#find common ancestor 
	#assume v1 < v2
	#find mom > v1 and mom < v2 and continue
	def Solve46(self, a1, a2):
		node = None
		tree = self.buildTree()

		node1 = tree.find(a1)
		node2 = tree.find(a2)

		if (node1 is None or node2 is None):
			return

		cur1 = node1
		cur2 = node2

		v1 = a1
		v2 = a2

		while True: 
			#find next mom1 > v2 and next mom2 > v2
			#make sure mom1.value not > mom2.value
			#check every step to get mom1.value == mom2.value
			while (cur1.mom is not None):
				if (cur1.mom.value > cur2.value):
					break

				if cur1.value > v1:
					break
				else:
					cur1 = cur1.mom

			while (cur2.mom is not None):
				if cur2.value < v2:
					break
				else:
					cur2 = cur2.mom

			v1 = cur1.value
			v2 = cur2.value


			if cur1.value == cur2.value:
				node = cur1
				break

			if cur1.value > cur2.value:
				break

		if (node is not None):
			print('common ancestor of: ', a1, '-', a2, ' is: ', node.value)


	def Solve47(self):
		bTree = self.buildTree()
		sTree = self.buildSubTree()

		rValue = sTree.root.value
		bnode = bTree.find(rValue)
		snode = sTree.root

		if (bnode is not None):
			print('node is found')
			isSubTree = self.subtree(bnode, snode)
			if isSubTree:
				print('is a subtree')
			else:
				print('not a subtree')

	def subtree(self, bnode, snode):
		if snode is None:
			return True

		if bnode is None:
			return False

		if (bnode.value == snode.value):
			return self.subtree(bnode.left, snode.left) and self.subtree(bnode.right, snode.right)
		else:
			return False

	def Solve48(self, sum):

		tree = self.buildTree()
		rnode = tree.root

		self.traverse(rnode, sum)

	def traverse(self, rnode, sum):
		if rnode is None:
			return

		#print('trace from node: ', rnode.value)
		arr = []
		self.trace(sum, rnode, arr)

		self.traverse(rnode.left, sum)
		self.traverse(rnode.right, sum)

	def trace(self, residue, node, arr=[]):
		if (node is None):
			arr.pop()
			return

		if residue == node.value:
			print('found end node: ', node.value)
			arr.append(node.value)
			print(list(arr))
			return

		arr.append(node.value)
		residue = residue - node.value

		arr1 = arr[:]
		if (node.mom is not None and node.mom.value not in arr1):
			self.trace(residue, node.mom, arr1)

		arr2 = arr[:]
		if (node.left is not None and node.left.value not in arr2):
			self.trace(residue, node.left, arr2)

		arr3 = arr[:]
		if (node.right is not None and node.right.value not in arr3):
			self.trace(residue, node.right, arr3)


	def buildTree(self):
		#create tree
		arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
		tree = Tree()
		for i in arr:
			tree.add(i)
		return tree

	def buildSubTree(self):
		#create tree
		#arr = [3, 1, 6, 4, 7]
		arr = [10, 6, 14]

		tree = Tree()
		for i in arr:
			tree.add(i)
		return tree

	def showValue(self, nodes):
		for i in nodes:
			print(i.value, end=' ')
		print()



test = Chapter4()
test.Solve48(17)




