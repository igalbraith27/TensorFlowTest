import tensorflow as tf

# Model Params
X = tf.Variable([.3], tf.float32)
Y = tf.Variable([-.3], tf.float32)

#Input/Outputs
node1 = tf.placeholder(tf.float32)

model_lin = X * node1 + Y

node2 = tf.placeholder(tf.float32)

# Loss
dela_sq = tf.square(model_lin - y)
loss = tf.reduce_sum(dela_sq)

## OPTIMIZE:
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

#Init
sesh = tf.Session()
init = tf.global_variables_initializer();
sesh.run(tf.global_variables_initializer())

#run
for x in range(1000):
    sesh.run(model_lin, {node1:[1, 2, 3, 4] node2:[0, -1, -2, -3]})


print(X)
print(Y)
#print(sesh.run(model_lin, {node1:[1, 2, 3, 4] node2:[0, -1, -2, -3]}))
