from BST import BSTNode
from BST import BST
from DLL import DLLNode
from DLL import DLL

class Solution:

	#find row has max num of 1
	def sol1(self):
		arr = self.buildS1()

		l = len(arr)
		x = len(arr[0])
		i1 = len(arr[0])
		r = 0
		#use binary search to find 1
		for i in range(l):
			row = arr[i]
			tmp = self.find1(0, x - 1, row)
			if (tmp < i1 and tmp > -1):
				r = i
				i1 = tmp

		print('->' , r)

	#find idx of first 1 (binary)
	def find1(self, start, end, arr = []):


		if (start == end - 1):
			if (arr[start] == 1):
				return start
			elif (arr[end] == 1):
				return end
			else:
				return -1


		mid = int(round(float(start + end) / 2))
		if (arr[mid] == 1):
			return self.find1(start, mid, arr)
		else:
			return self.find1(mid, end, arr)


	def buildS1(self):
		arr = [] 
		arr.append([0, 1, 1, 1]);
		arr.append([0, 0, 1, 1]);
		arr.append([1, 1, 1, 1]);
		arr.append([0, 0, 0, 0]);

		return arr

	#find and print longest sequence
	'''
	Ex: Input: 1 2 5 3 6 8 7
       Output: 5 6 7 8 
    '''
	def sol2(self):
		arr = self.build2()
		arr = self.sort(0, len(arr) - 1, arr)

		maxSeq = -1
		startIdx = 0

		tmpSeq = []

		seq = 1
		idx = 0

		arr.append(None)

		running = False

		for i in range(len(arr)):
			if i > 0:

				if (arr[i] is not None and arr[i] - arr[i-1] == 1):
					seq += 1
					if (running == False):
						idx = i - 1
						running = True

				elif (arr[i] is None or (arr[i] - arr[i - 1] != 1)):

					running = False
					if maxSeq < seq:
						maxSeq = seq
						startIdx = idx
					seq = 1

		for j in range(startIdx, startIdx + maxSeq):
			print(arr[j], end=' ')

	def findSequence(self):
		pass

	#merge sort
	def sort(self, start, end, arr = []):

		if (start == end):
			tmpArr = [] 
			tmpArr.append(arr[start])
			return tmpArr

		mid = round(float(start + end) / 2)

		left = self.sort(start, mid, arr)
		right = self.sort(mid + 1, end, arr)

		return self.merge(left, right)

	#merge 2 sorted arr
	def merge(self, left, right):
		pad = left[:] + len(right) * [None]

		li = len(left) - 1
		lr = len(right) - 1
		lp = len(pad) - 1

		while (li >= 0 and lr >= 0):
			if (left[li] > right[lr]):
				pad[lp] = left[li]
				li -= 1
			else:
				pad[lp] = right[lr]
				lr -= 1

			lp -= 1

		return  pad


	def build2(self):
		return [1, 2, 5, 3, 6, 8, 7]


	#convert BST to DDL
	def sol3(self):
		tree = BST()
		arr = [30, 20, 40, 10, 37, 45, 12]

		for n in arr:
			tree.add(n)

		tree.inOrder(tree.root)
		print('convert tree to double link list')
		dll = DLL()
		self.convert3(dll, tree.root)
		dll.trace()

		print('\nconvert back the dll to balanced tree')
		tree = BST()

		self.convertDllToTree(tree, dll, 0, dll.count - 1)
		'''
		n = dll.count
		self.sortedDLLToBST(tree, dll, n)
		'''

		tree.levelOrder()


	def convert3(self, dll, node):
		if (node is None):
			return

		self.convert3(dll, node.left)
		dll.add(node.value)
		self.convert3(dll, node.right)

	#method 1:
	def convertDllToTree(self, tree, dll, start, end):
		if (start == end - 1 or start == end):
			value = self.getValueAt(dll, start)
			tree.add(value)
			print('return')
			return

		mid = int(round(float(start + end) / 2))
		value = self.getValueAt(dll, mid)
		tree.add(value)

		self.convertDllToTree(tree, dll, start, mid - 1)
		self.convertDllToTree(tree, dll, mid + 1, end)

		return tree

	#method 2: FAILED
	def sortedDLLToBST(self, tree, dll, n):

		if n <= 0:
			return None

		print('n: ', n)
		#input()

		rootValue = dll.head.value

		if (dll.head is not None):
			print('add root: ', rootValue)
			tree.add(rootValue)


		print('left')
		leftValue = self.sortedDLLToBST(tree, dll, int(n/2))

		if (leftValue is not None):		
			tree.add(leftValue)	

		dll.head = dll.head.next

		rightValue = self.sortedDLLToBST(tree, dll, n - int(n/2) - 1)

		if (rightValue is not None):
			tree.add(rightValue)

		return rootValue


	def getValueAt(self, dll, i):
		cur = dll.head

		if (dll.count <= i):
			return None

		while (i > 0):
			i -= 1
			cur = cur.next

		#print("get value at: ", i, ' -> ', cur.value)
		return cur.value


	#Given an array, Find a triplet a, b, c such that a2 = b2 + c2
	#similiar to  Find a pair with given sum
	#use hashing
	def sol4(self):
		arr = [9, 2, 3, 4, 8, 5, 6, 10]

		


test = Solution()
test.sol3()
