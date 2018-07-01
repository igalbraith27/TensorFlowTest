import tensorflow as tf

# Model Params
X = tf.Variable([.2], tf.float32)
Y = tf.Variable([-.2], tf.float32)

#Input/Outputs
node1 = tf.placeholder(tf.float32)

model_lin = X * node1 + Y

node2 = tf.placeholder(tf.float32)

# Loss
dela_sq = tf.square(model_lin - y)
loss = tf.reduce_sum(dela_sq)

#Init
sesh = tf.Session()
sesh.run(tf.global_variables_initializer())

print(sesh.run(model_lin, {node1:[1, 2, 3, 4] node2:[0, -1, -2, -3]}))
