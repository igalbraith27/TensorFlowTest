import tensorflow as tf


node1 = tf.constant(3.0)
node2 = tf.constant(4.0)


sesh = tf.Session()
node3 = a * b

with tf.Session as sesh:
    output = sesh.run([node1,node2])
    print(output)
    output = sesh.run(node3)
    print(output)
