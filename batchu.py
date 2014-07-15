class Batchu:
	def solve(self, s1, c):
		tmp = list(s1)
		pass

	#get num of character from arr
	def build(self, num, arr=[]):
		pass	

	def permute(self, s="", arr=[]):

		if (len(arr) == 2):
			tmp = (s + str(arr[0]) + str(arr[1]))
			self.filter(tmp)
			#print(tmp)

			tmp = (s + str(arr[1]) + str(arr[0]))
			self.filter(tmp)
			#print(tmp)
			return
		else:

			for x in arr:
				tmpArr = arr[:]
				tmpArr.remove(x)
				s += str(x)
				self.permute(s, tmpArr)
				#back character
				s = s[:-1]

	def combine(self, num, arr=[]):
		l = len(arr)
		if num >= l:
			result = ''.join(arr)
			print(result)

		#pointer array
		pArr = []
		for i in range(num):
			pArr.append(i)

		print(pArr)

		#pointer
		p = num - 1
		end = l - 1 
		moveP = False

		while 1:
			result = ""

			if not moveP:
				for i in pArr:
					result += arr[i]
				self.process(result)

			if pArr[p] < end:
				pArr[p] += 1
				moveP = False
			else:
				end -= 1
				p -= 1
				moveP = True
				if (p < 0):
					break

			if (pArr[0] > l - num):
				break;

	def filter(self, string):
		l = len(string)
		string = string.lower()

		#3 first characters is not vowel
		if (l >= 3):
			if (not self.isCharacterVower(string[0]) 
				and not self.isCharacterVower(string[1]) 
				and not self.isCharacterVower(string[2])):
				return

		if (l >= 4):
			if (self.isCharacterVower(string[l - 1])):
				return
			if (not (string[l - 1] == "h" or string[l - 1] == "g")):
				return
			if (not (string[l - 2] == "n" or string[l - 2] == "c")):
				return		

			if (not self.isCharacterVower(string[l - 3])):
				return

			if (l >= 5):	
				if (self.isCharacterVower(string[0])):
					return

		if (l == 1):
			if (not self.isCharacterVower(string[0])):
				return

		if (l == 3):
			if (self.isCharacterVower(string[1]) and self.isCharacterVower(string[2])):
				return

			if (not self.isCharacterVower(string[2]) and not self.isCharacterVower(string[1])):
				tmp = string[1] + string[2]
				if(not (tmp == "kh" or tmp == "ng" or tmp == "ch" or tmp == "nh" or tmp == "tr")):
					return

		if (not self.isVowel(string)):
			return

		print(string)


	def process(self, string):
		self.permute("", list(string))


	def isVowel(self, string):
		for c in string:
			tmp = c.lower()
			if (tmp == 'a' or tmp == 'o' or tmp == 'u' or tmp == 'i' or tmp == 'y' or tmp == 'e'):
				return True

		return False

	def isCharacterVower(self, tmp):
		tmp = tmp.lower()
		return (tmp == 'a' or tmp == 'o' or tmp == 'u' or tmp == 'i' or tmp == 'y' or tmp == 'e')


test = Batchu()
string = "GLUANTDHREUTIH"


tmp = list("OEDNTNUQIGA")
test.combine(4, tmp)

#test.permute("", tmp)
