class Chapter9:

	#O(n^2)
	def bubbleSort(self, arr=[]):

		tmpArr = arr[:]
		
		if (len(tmpArr) >= 2):
			l = len(tmpArr)
			for i in reversed(range(0,l)):
				for j in range(0, i):
					if (tmpArr[j] > tmpArr[j+1]):
						tmp = tmpArr[j]
						tmpArr[j] = tmpArr[j + 1]
						tmpArr[j + 1] = tmp

		self.printArr(tmpArr)
		
	#o(n^2)
	def selectionSort(self, arr=[]):
		tmpArr = arr[:]
		if (len(tmpArr) < 2):
			self.printArr(tmpArr)
			return

		#find smallest and push to front
		for i in range(0, len(tmpArr)):

			minVal = tmpArr[i]
			minIdx = i

			for j in range(i, len(tmpArr)):
				if (minVal > tmpArr[j]):
					minVal = tmpArr[j]
					minIdx = j
			#push to front
			tmp = tmpArr[i] 
			tmpArr[i] = tmpArr[minIdx]
			tmpArr[minIdx] = tmp

		self.printArr(tmpArr)			

	#O(nxlogn)
	def mergeSort(self, arr=[]):
		#divide to sub array with only 2 items, sort and merge them
		tmpArr = arr[:]
		if (len(tmpArr) < 2):
			self.printArr(tmpArr)
			return

		result = self.ms_sort(0, len(tmpArr) - 1, tmpArr)
		self.printArr(result)

	def ms_sort(self, start, end, arr=[]):

		if (start == end):
			tmp = []
			tmp.append(arr[start])
			return tmp
		
		mid = int((start + end) / 2)
		left = self.ms_sort(start, mid, arr)
		right = self.ms_sort(mid + 1, end, arr)

		return self.ms_merge(left, right)

	#return merge sorted array	
	def ms_merge(self, left=[], right=[]):

		tmp = []

		i = 0
		j = 0
		L = len(left) + len(right)
		check = True

		for a in range(0, L):

			if (i >= len(left)):
				check = False
				tmp.append(right[j])
				j += 1

			elif (j >= len(right)):
				check = False
				tmp.append(left[i])
				i += 1

			if (check):
				if (left[i] > right[j]):
					tmp.append(right[j])
					j += 1
				else:
					tmp.append(left[i])
					i += 1	

		return tmp

	#complicate: cannot remember
	def quickSort(self, arr=[]):
		pass

	#or bin sort
	#O(n + m): best
	def bucketSort(self, noBucket, arr=[]):

		#build buckets
		buckets = []
		for i in range(noBucket):
			tmp = [] 
			buckets.append(tmp)

		tmpArr = arr[:]
		#find max value
		maxValue = arr[0]
		for nu in tmpArr:
			if maxValue < nu:
				maxValue = nu

		for nu in tmpArr:
			no = int(nu / ((maxValue + 1) / noBucket))
			#append sort here
			#best time for sort is when each bin has only 1 value
			if (len(buckets[no]) == 0):
				buckets[no].append(nu)
			else:
				tmp = buckets[no][:]
				buckets[no] = []
				added = False
				for j in tmp:
					if (j > nu):
						buckets[no].append(nu)
						added = True
					buckets[no].append(j)
				if (not added):
					buckets[no].append(nu)


		#complexity for merge = m (m is distint value)
		result = []
		for b in buckets:
			for number in b:
				result.append(number)

		self.printArr(result)		

	def printArr(self, arr=[]):
		for i in arr:
			print(i, end=' ')

		print()

	'''exercises'''
	def Exercise91(self, left=[], right=[]):
		i = 0
		for nr in right:
			while (left[i] is not None and nr > left[i]):
				i += 1

			if (left[i] is None):
				left[i] = nr
				i += 1
			#push elements to the right
			else:
				for j in reversed(range(i + 1, len(left))):
					if (left[j - 1] is not None):
						left[j] = left[j - 1]
				left[i] = nr

		self.printArr(left)

	#first check strings are anagrams
	#check anagram by sorting string and compare
	def Exercise92(self, strings=[]):
		print(strings)

		i = 0

		while (i < len(strings) - 1):

			for j in range(i + 1, len(strings)):
				if (self.E92_checkAnagram(strings[i], strings[j])):
					tmp = strings[i + 1] 
					strings[i + 1] = strings[j]
					strings[j] = tmp
					i += 1

			i += 1

		print(strings)

	def E92_checkAnagram(self, s1, s2):
		if (len(s1) != len(s2)):
			return False
		return self.E92_sortS(s1) == self.E92_sortS(s2) 
			

		return True
	def E92_sortS(self, s):
		l = list(s)
		#bubbleSort
		for i in reversed(range(1, len(l))):
			for j in range(i):
				if (l[j] < l[j + 1]):
					tmp = l[j]
					l[j] = l[j + 1]
					l[j + 1] = tmp

		return ''.join(l)
		
	#end Exercise92

	def Exercise93(self, number, arr=[]):
		idx = -1
		newArr = []

		start = 0
		mid = -1 
		end = len(arr) - 1
		mid = int((start + end) / 2) 

		if (arr[end] == number):
			print(number, '=>', end)
			return

		if (arr[start] == number):
			print(number, '=>', start)
			return

		while (mid != start and mid != end):

			#print('mid: ', mid, 'start: ' , start, 'end: ', end)
			
			if (arr[mid] == number):
				idx = mid
				break

			if (arr[start] > arr[end]):
				#mid < start and mid > start
				if (arr[start] < arr[mid]):
					if (number < arr[mid]):
						end = mid
					else:
						start = mid
				else:
					#right
					if (arr[mid] < number and arr[end] > number):
						start = mid
					else:
						end = mid
			else:
				#left
				if (arr[mid] > number):
					end = mid
				else:
					start = mid


			mid = int((start + end) / 2)

		print(number, '=>', idx)



#test bed
testArr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
test = Chapter9()

for nu in testArr:
	test.Exercise93(nu, testArr)

'''
arr = ['123', '55', '77', '88', '231', '55', '55', '99', '312']
test.Exercise92(arr)

print('bubble sort')
test.bubbleSort(testArr)

print('selection sort')
test.selectionSort(testArr)

print('merge sort')
test.mergeSort(testArr)

print('bucket sort')
test.bucketSort(5, testArr)


left = [1, 5, 7, None, None, None]
right = [2, 6, 8]

test.Exercise91(left, right)
'''

