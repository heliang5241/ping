#encoding:utf-8
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n,'=', x, '*', n//x)
			break
	else:
	#这是正确的代码。看仔细：else 语句是属于 for 循环之中， 不是 if 语句。
		print(n,'is a prime number')																																																										