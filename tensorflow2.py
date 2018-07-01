import tensorflow as tf


node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)

adder = node1 + node2

sesh = tf.Session()

print(sesh.run(adder, {a:[2, 3], b:[2, 1]}))
