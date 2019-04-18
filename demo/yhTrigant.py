def triangles():
	b = [1]
	while True:
		yield b
		for i in range(2 - 1):
			print(i)
		b = [1] + [b[i] + b[i+1] for i in range(len(b) - 1)] + [1]


p = triangles()
n = 0
while n < 9:
	print(next(p))
	n+=1