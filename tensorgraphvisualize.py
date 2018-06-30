import tensorflow as tf


node1 = tf.constant(3.0)
node2 = tf.constant(4.0)


sesh = tf.Session()
node3 = a * b
File_Writer = tf.summary.FileWriter("C:\\Users\\Ian\\Documents\\GitHub\\TensorFlowTest\\TensorFlowTest\\graph", sesh.graph)
with tf.Session as sesh:
    output = sesh.run(node3)
    print(output)
