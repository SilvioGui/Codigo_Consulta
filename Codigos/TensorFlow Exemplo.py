import tensorflow as tf

# Define the model
x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])
w = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
pred = tf.add(tf.multiply(x, w), b)

# Define the loss function and optimizer
loss = tf.reduce_mean(tf.square(pred - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Generate some fake data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# Training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        _, l = sess.run([optimizer, loss], feed_dict={x: x_data, y: y_data})
        if i % 100 == 0:
            print('Step %d, Loss: %f' % (i, l))

    # Testing
    w_out, b_out = sess.run([w, b])
    print('Weight: %f, Bias: %f' % (w_out, b_out))
