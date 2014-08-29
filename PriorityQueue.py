#implement using min-heap
class PriorityQueue:
	def __init__(self):
		self.__arr = []
		self.__arr.append(None)

	def add(self, n):
		self.__arr.append(n)

		#bubble up
		cI = len(self.__arr) - 1
		pI = self.getParentI(cI)

		while (pI != -1):
			#compare and swap
			if (self.__arr[cI] < self.__arr[pI]):
				tmp = self.__arr[cI]
				self.__arr[cI] = self.__arr[pI]
				self.__arr[pI] = tmp

				cI = pI
				pI = self.getParentI(cI)
			else:
				break

	def removeMin(self):
		#replace 1 with last and bubble down
		if (len(self.__arr) == 1):
			return 

		if (len(self.__arr) == 2):
			self.__arr.pop()
			return

		last = self.__arr.pop()
		self.__arr[1] = last

		#bubble down
		curI = 1
		childI = self.getMinChildI(curI)

		while (childI != -1):
			#swap
			tmp = self.__arr[curI]
			self.__arr[curI] = self.__arr[childI]
			self.__arr[childI] = tmp

			curI = childI
			childI = self.getMinChildI(curI)


	def getMinChildI(self, i):
		left = self.getLI(i)
		right = self.getRI(i)

		if (left == -1):
			return -1

		if (right == -1):
			return left

		tmp = left
		if (self.__arr[left] > self.__arr[right]):
			tmp = right

		if (self.__arr[i] < self.__arr[tmp]):
			return -1
		else:
			return tmp


	def peekMin(self):
		min = None
		if (len(self.__arr) > 1):
			min = self.__arr[1]
		print('peekMin -> ', min)
		return min

	#helpers
	def show(self):
		print(self.__arr)

	def getParentI(self, i):
		if (i == 1):
			return -1

		if (i%2 == 0):
			return int(i/2)
		else:
			return int((i-1)/2)

	def getLI(self, i):
		if (2*i >= len(self.__arr)):
			return -1
		else:
			return 2*i

	def getRI(self, i):
		if (2*i + 1 >= len(self.__arr)):
			return -1
		else:
			return 2*i + 1		

'''test'''
test = PriorityQueue()
inputs = [1, 17, 19, 36, 2, 3]
for n in inputs: 
	test.add(n)

test.show()
test.peekMin()
test.removeMin()
test.show()
