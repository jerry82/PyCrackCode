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
				for j in tmp:
					if (j > nu):
						buckets[no].append(nu)
					buckets[no].append(j)

		#complexity for merge = m (m is distint value)
		result = []
		for b in buckets:
			for number in b:
				result.append(number)

		self.printArr(result)

		#self.printArr(buckets)
		

	def printArr(self, arr=[]):
		for i in arr:
			print(i, end=' ')

		print()


#test bed
testArrError = [1]
testArr = [1, 5, 10, 6, 9, 8, 3, 7]
test = Chapter9()

print('bubble sort')
test.bubbleSort(testArr)

print('selection sort')
test.selectionSort(testArr)

print('merge sort')
test.mergeSort(testArr)

print('bucket sort')
test.bucketSort(5, testArr)


