class Chapter5:
	def test(self):
		print("test")

	def E51(self, N, M, i, j):
		if (j - i + 1 != len(M)):
			print('failed')
			return

		A = int(N, 2)
		B = int(M, 2)

		left = A >> (j + 1)
		left = left << (j + 1)
		r = A - (A >> i << i)
		c = r + left
		d = B << i
		e = c + d

		print(bin(e))
		

	#print a decimal binary number
	def E52(self, dec):
		n = int(dec) 
		d = (dec - float(n))
		d = float('{0:.6g}'.format(d))
		display = self.E52ConvertToBin(n) + '.' + self.E52ConvertToBin(d)
		print(display)

	def E52ConvertToBin(self, i):
		c = []
		tmp = i
		#limit 10 decimal number
		maxTrailing = 15
		needReverse = True

		if (i < 1 and i > 0):
			j = 1
			tmp = i
			needReverse = False
			while (j < maxTrailing):
				a = 1 / (2 ** j)
				if (tmp > a):
					c.append(1)
					tmp -= a
					#print(tmp)
				elif (tmp < a):
					c.append(0)
				else:
					c.append(1)
					break;

				j += 1

		else:
			#positive
			if (i > 0):
				while (tmp != 0):
					r = tmp % 2
					c.append(r)
					tmp = int(tmp / 2)
			elif (i == 0):
				c.append(0)


		if (needReverse):
			c = reversed(c)
		display = ''.join(str(x) for x in c)
		#print(display)
		return display

	def E53(self, N):
		strNum = self.E52ConvertToBin(N)
		l = len(strNum)
		strL = list(strNum)

		print('ori: ', strNum)
		print(strL)

		#find next bigger
		#swap bit
		found1 = False
		no1 = 0
		idx = 0
		for i in reversed(range(0, l)):
			tmp = strNum[i]
			if tmp == '1':
				no1 += 1
				found1 = True
			elif found1:
				strL[i] = '1'
				strL[i + 1] = '0'
				idx = i + 1
				break

		#move 1s to the right
		no1 -= 1
		if idx < l - 1:
			for i in reversed(range(idx,l)):
				if no1 > 0:
					strL[i] = '1'
					no1 -=1 
				else:
					strL[i] = '0'
			
		print('next bigger: ', "".join(strL))

		#find next smaller


test = Chapter5()
test.E53(5)





