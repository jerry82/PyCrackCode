
class DLLNode:
	def __init__(self, value):
		self.__value = value
		self.__prev = None
		self.__next = None

	@property 
	def value(self):
		return self.__value

	@value.setter
	def value(self, value):
		self.__value = value

	@property 
	def prev(self):
		return self.__prev

	@prev.setter
	def prev(self, node):
		self.__prev = node

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, node):
		self.__next = node

import copy

class DLL:
	def __init__(self):
		self.__head = None
		self.__tail = None
		self.__count = 0

	@property
	def count(self):
		return self.__count

	@property 
	def head(self):
		return self.__head

	def add(self, value):
		if (self.__count == 0):
			self.__head = DLLNode(value)
			self.__tail = self.__head
			self.__count = 1
			return

		tmp = copy.copy(self.__tail)
		self.__tail.next = DLLNode(value)
		self.__tail = self.__tail.next
		self.__tail.prev = tmp
		self.__count += 1

	def trace(self):
		if self.__head == None:
			return

		cur = self.__head 
		while (True):
			print(cur.value, end="")
			tmp = copy.copy(cur)
			cur = cur.next

			if (cur == None):
				break

			if (cur.prev != None and cur.prev.value == tmp.value):
				print(" <-> ", end="")
			else:
				print(" -> ", end="")


'''test'''
'''
test = DLL()
for i in range(10):
	test.add(i)

test.trace()
'''






