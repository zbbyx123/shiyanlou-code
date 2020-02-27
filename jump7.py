a = 1
while a < 101:
	if a%7 == 0 :
		pass
	elif a%10 == 7:
		pass
	elif a//10 == 7:
		pass
	else:
		print(a)
	a = a + 1
