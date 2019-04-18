import numpy as np

x = np.arange(4)
y = 3
#print(x)
#print(x[1:y])
#print(x[1:y:4])
#arr_slice = x[1:3]
#print(arr_slice)
#print(arr_slice[:])

xx = x.reshape(2, 2)

#print('xx', xx, xx.shape)

y = np.arange(35).reshape(5, 7)
#print(y)

for i in range(100): 
	xs = np.array([[i]])
	ys = np.array([[2*i]])
	#print('xs:', xs)
	#print('ys:', ys) 

def testFun():
	temp = [lambda x : i*x for i in range(4)]
	return temp
print(testFun)	
for everyLambda in testFun():
	print(everyLambda(2))

foo = range(1,4)
print([i for i in foo])
print(foo)	