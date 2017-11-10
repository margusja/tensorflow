import tensorflow as tf

a = tf.constant(10)
b = tf.constant(20)
c = tf.constant(30)
d = tf.constant(40)
e = tf.add(a,b)
f = tf.subtract(c,d)
h = tf.multiply(e,f)
sess = tf.Session()
print(sess.run(h))
