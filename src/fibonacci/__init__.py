def fibonacci(n):
	a = 1
	b = 1

	for i in range(2, n):
		print(i)

		b = a
		a = a + b

	print(a)





fibonacci(10)
