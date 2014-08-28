class jNode:
	def __init__(self, value):
		self.__value = value
		self.__next = None

	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self, value):
		self.__value = value

	@property 
	def next(self):
		return self.__next

	@next.setter
	def next(self, node):
		self.__next = node

class jlList:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__count = 0

	@property
	def head(self):
		return self.__head

	def count(self):
		return self.__count

	def add(self, node):
		if (self.__head is None):
			self.__head = node
			self.__tail = self.__head
		else:
			self.__tail.next = node
			self.__tail = node

		self.__count += 1

	def delete(self, value):
		
		if (self.__count == 0):
			return

		#1 element
		if (self.__count == 1):
			if (self.__head.value == value):
				self.__head = None
				self.__tail = None
				self.__count = 0
				return

		curNode = self.__head
		prevNode = None

		while curNode is not None:
			if (curNode.value == value):
				#delete head
				if (prevNode is None):
					self.__head = self.__head.next
				else:
					prevNode.next = curNode.next

				self.__count -= 1
				return


			else:
				prevNode = curNode
				curNode = curNode.next 

	def find(self, value):
		pos = 0

		curNode = self.__head
		while (curNode is not None):
			if (curNode.value == value):
				return pos
			else:
				pos += 1
				curNode = curNode.next

		return -1

	def traverse(self):
		curNode = self.__head
		while (curNode is not None):
			print(curNode.value, '-', end='')
			curNode = curNode.next
		print('count:', self.__count)

class amCheat:
	'''
	1)	There is a linked lists L1. Write an algorithm that check whether L1 has loop and find the starting point 
	of the loop.

	Ans:
	=> user 2 pointers moving at different speed. 
	1st at 1 node at a time
	2nd at 2 nodes at a time
	they will meet somewhere in the Loop (if there is) Xl.

	X0: start of the linked lists
	Xs: starting point of the loop

	distance: 
	a = X0->Xs
	b = Xs->Xl
	l = length of the loop

	=> 2*(a + b) = (a + b) + n*l 
	=> a + b = n*l
	=> a = (n - 1) * l + l - b   (***)
	l - b is the distance from Xl to Xs 

	from (***) => to find the starting point of the circle run 2 pointers at the same speed:
	1st at X0 
	2nd at Xl
	They will meet at the starting point of the Loop 
	 
	'''
	def findLoop(self):
		pass
	'''
	2) List Intersection ProblemGiven that, there are 2 linked lists L1 and L2. Write an algorithm that finds the point of 
	intersection of the two linked lists.'''
	def findIntersection(self):
		table = {}
		tmp1 = [3, 6, 9, 15, 30]
		tmp2 = [10, 15, 30]
		list1 = jlList()
		list2 = jlList()

		for i in tmp1:
			n1 = jNode(i)
			list1.add(n1)

		for i in tmp2:
			n2 = jNode(i)
			list2.add(n2)

		#start
		curNode = list1.head

		while (curNode is not None):
			if curNode.value not in table:
				table[curNode.value] = 1
			curNode = curNode.next

		curNode = list2.head
		while (curNode is not None):
			if curNode.value in table:
				print(curNode.value)
				return
			curNode = curNode.next

	'''      
	    3) Given 2 arrays of numbers find if each of the two arrays have
		the same set of integersGiven 2 arrays of numbers find if each of the two
		arrays have the same set of integers? Suggest an algorithm which can run
		faster than NlogN.    

		Ans:
		Use the hash table to store all element of list1 O(n). 
		Keys are unique interger and values are the no of appearance of that interger in list1
		Iterate through list2 and check the appearance, minus 1 in value if found same key O(n), quit if any interfer from list2
		not in list1
		Check if all values of the hash table is 0

	'''
	def isSameSet(self):
		list1 = [1, 2, 3, 4, 5, 1, 2] 
		list2 = [3, 2, 1, 5, 4, 1, 2]

		if (len(list1) != len(list2)):
			return False

		table = {}

		for nu in list1:
			if nu in table:
				table[nu] += 1
			else:
				table[nu] = 1

		for nu in list2:
			if nu not in table:
				return False
			else:
				table[nu] -= 1


		for key in table:
			if table[key] != 0:
				return False


		return True

	'''
	4. I have an array consisting of 2n+1 elements. n elements in it are married, i.e they occur twice in the array, however there is one element which only appears once in the array. I need to find that number in a single pass using constant memory. {assume all are positive numbers}
	Eg : 3 4 1 3 1 7 2 2 4
	=>: 7
	'''
	def findX(self):
		list1 = [3, 4, 1, 3, 1, 7, 2, 2, 4]
		tmp = 0

		if (len(list1) == 1):
			return list1[0]
		else:
			for nu in list1:
				tmp = tmp ^ nu

		return tmp
	
	'''
	5) Find common elements in 2 unique sorted array
	Ans: use 2 pointers and move 2 pointers to the right.
	if list[p1] > list[p2] then move p2 and vice versa
	'''
	def findCommon(self):
		list1 = [1, 3, 4, 5, 6, 8]
		list2 = [4, 5, 6, 7, 8, 10, 15]

		p1 = 0
		p2 = 0

		while (p1 < len(list1) and p2 < len(list2)):
			if (list1[p1] == list2[p2]): 
				print(list1[p1])
				p1 += 1 

			elif (list1[p1] > list2[p2]):
				p2 += 1
			else:
				p1 += 1

	'''
	6)
	'''




#test bed
test = amCheat()
test.findCommon()
