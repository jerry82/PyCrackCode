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


	def ms_merge(self, left=[], right=[]):
		tmp = left[:] + [None] * len(right) 

		iL = len(left) - 1
		iR = len(right) - 1
		L = len(tmp) - 1

		while (iL >= 0 and iR >= 0):
			if (left[iL] > right[iR]):
				tmp[L] = left[iL]
				iL -= 1
			else:
				tmp[L] = right[iR]
				iR -= 1

			L -= 1

		while (iL >= 0):
			tmp[iL] = left[iL]
			iL -= 1

		while (iR >= 0):
			tmp[iR] = right[iR]
			iR -= 1

		return tmp

	#complicate: cannot remember
	def quickSort(self, arr=[]):
		pass


	def heapSort(self, arr=[]):
		tmp = []
		curIdx = 0

		#build a heap array 
		for num in arr:			
			tmp.append(num)

			#arrange
			tmpCur = curIdx
			iM = self.hs_getMom(tmpCur)

			while (iM != -1):
				if (tmp[iM] < tmp[tmpCur]):
					tmpNum = tmp[iM] 
					tmp[iM] = tmp[tmpCur]
					tmp[tmpCur] = tmpNum

				tmpCur = iM
				iM = self.hs_getMom(tmpCur)

			curIdx += 1
		
		#sort
		iD = len(tmp) - 1
		while (iD >= 0):
			#swap last and first element
			if (tmp[iD] < tmp[0]):
				tmpNu = tmp[0]
				tmp[0] = tmp[iD]
				tmp[iD] = tmpNu

			iD -= 1

			#move the new top element to bottom
			cur = 0
			iL = self.hs_getLeft(cur)
			iR = self.hs_getRight(cur)

			while (iL <= iD or iR <= iD):

				#has 2 children
				if (iR <= iD):
					if (tmp[iL] > tmp[iR]):
						tmpX = iL
					else:
						tmpX = iR
				#has 1 child
				else:
					tmpX = iL

				#swap and assign new cur
				tmpNu = tmp[tmpX] 
				tmp[tmpX] = tmp[cur]
				tmp[cur] = tmpNu

				cur = tmpX
				iL = self.hs_getLeft(cur)
				iR = self.hs_getRight(cur)

		print(tmp)

	def hs_getLeft(self, curIdx):
		return curIdx * 2 + 1

	def hs_getRight(self, curIdx):
		return curIdx * 2 + 2

	def hs_getMom(self, curIdx):
		if (curIdx == 0):
			return -1;
		if (curIdx % 2 != 0):
			return int((curIdx - 1) / 2)
		else: 
			return int((curIdx - 2) / 2)

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
	def Exercise91a(self, left=[], right=[]):
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

	#complexity = len(left)
	def Exercise91(self, left=[], right=[]):

		la = 0
		lb = len(right) - 1
		l = len(left) - 1

		#assume la > lb
		for i in reversed(range(len(left))):
			if (left[i] is not None):
				la = i
				break;

		#sort from the righ most
		while (la >= 0 and lb >= 0):
			if (left[la] > right[lb]):
				left[l] = left[la]
				la -= 1
			else:
				left[l] = right[lb]
				lb -= 1
			
			l -= 1

		while (lb >= 0):
			left[lb] = right[lb]
			lb -= 1

		print(left)

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

	#search sort strings with empty str in between
	def Exercise95(self, inputStr, arr=[]):
		result = self.Search95(inputStr, 0, len(arr) - 1, arr)
		print(result)

	global times
	times = 0
	#recursive if stuck at "" then search left and right
	def Search95(self, inputStr, start, end, arr=[]):

		global times
		times += 1
		print("executed: ", times)

		if (start == end):
			if (arr[start] == inputStr):
				return start
			else:
				return -1

		mid = int((start + end) / 2)

		if (arr[mid] == inputStr):
			return mid

		if (arr[mid] == ""):
			tmpL = self.Search95(inputStr, start, mid - 1, arr)
			if (tmpL == -1):
				return self.Search95(inputStr, mid + 1, end, arr)
			else:
				return tmpL
			
		elif (arr[mid] > inputStr):
			return self.Search95(inputStr, start, mid - 1, arr)
		else:
			return self.Search95(inputStr, mid + 1, end, arr)
	
	def Exercise96(self, num, arr=[]):
		'''
		tmp = [6, 7, 8, 9, 10]
		result = self.Search96(18, 0, len(tmp) - 1, tmp)
		print(result)
		'''
		
		resultJ = -1

		col = len(arr[0]) - 1 

		for i in range(len(arr)):
			tmp = arr[i]

			resultI = -1
			resultJ = -1

			if (tmp[0] <= num and tmp[col] >= num):
				resultI = i
				resultJ = self.Search96(num, 0, col, tmp)

				if (resultJ > -1):
					print(resultI, resultJ)

			if (tmp[0] > num):
				break;


	def Search96(self, num, jstart, jend, arr=[]):
		if (jstart == jend):
			if arr[jstart] == num:
				return jstart
			else:
				return -1

		mid = int((jstart + jend) / 2)
		if (arr[mid] == num):
			return mid
		elif(arr[mid] < num):
			return self.Search96(num, mid + 1, jend, arr)
		else:
			return self.Search96(num, jstart, mid - 1, arr)


	def Exercise97(self, arr=[]):
		
		#sort base on  0 idx
		l = len(arr)

		for i in reversed(range(l)):
			for j in range(0, i):
				if (arr[j][0] > arr[j + 1][0]):
					tmp = arr[j]
					arr[j] = arr[j + 1]
					arr[j + 1] = tmp
		cnt = 1
		tmp = arr[0][1]

		for k in range(1, l):
			if (arr[k][1] <= tmp):
				continue

			cnt += 1
			tmp = arr[k][1]


		print(cnt)


#test bed
arr = [6, 5, 3, 1, 8, 7, 2, 4]
test = Chapter9()
test.heapSort(arr);


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

