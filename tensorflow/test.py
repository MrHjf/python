#下载用于训练和测试的mnist数据集的源码

import input_data # 调用input_data
import tensorflow as tf
mnist = input_data.read_data_sets('data/', one_hot=True)
print("type of 'mnist' is %s" % (type(mnist)))
print("number of train data is %d" % (mnist.train.num_examples))
print("number of test data is %d" % (mnist.test.num_examples))
print("number of validation id %d" % (mnist.validation.num_examples))

x = tf.placeholder("float", [None, 784])

w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,w) + b)

y_ = tf.placeholder("float", [None,10])

cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  print(sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys}))