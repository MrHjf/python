import tensorflow as tf

x = tf.placeholder("float", [None, 784])

print(x)

a = tf.Variable(tf.zeros([1,2]));
print(a)

b = tf.zeros([784, 10]);
print(b)