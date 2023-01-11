#tensorflow.constant(): para criar tensores constantes (estruturas de dados básicas do TensorFlow) com valores específicos.
import tensorflow as tf

a = tf.constant(2)
b = tf.constant([1, 2, 3])
c = tf.constant([[1, 2], [3, 4]])

print(a)  # Tensor("Const:0", shape=(), dtype=int32)
print(b)  # Tensor("Const_1:0", shape=(3,), dtype=int32)
print(c)  # Tensor("Const_2:0", shape=(2, 2), dtype=int32)


#tensorflow.placeholder(): para criar tensores que servem como entradas para o modelo.
x = tf.placeholder(tf.float32, shape=(None, 2))
y = tf.placeholder(tf.float32, shape=(None, 1))

#tensorflow.Variable(): para criar tensores que representam os parâmetros do modelo.
w = tf.Variable(tf.random_normal([2, 1], stddev=0.1))
b = tf.Variable(tf.zeros([1]))

#tensorflow.add(), tensorflow.matmul() e outros operadores aritméticos: para realizar operações matemáticas em tensores.
a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a, b)

print(c)  # Tensor("Add:0", shape=(), dtype=int32)

#tensorflow.nn.relu(), tensorflow.nn.softmax() e outras funções de ativação: para adicionar não-linearidade aos modelos.

#tensorflow.train.GradientDescentOptimizer e outros otimizadores: para atualizar os parâmetros do modelo durante o treinamento.
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_op = optimizer.minimize(loss)

#tensorflow.losses.sparse_softmax_cross_entropy() e outras funções de custo: para calcular o erro do modelo durante o treinamento.
logits = ...  # A tensor of shape [batch_size, num_classes]
labels = ...  # A tensor of shape [batch_size]
loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)


#tensorflow.Session(): para iniciar uma sessão do TensorFlow, que é necessária para executar o cálculo em um grafo computacional.
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#session.run(): para executar operações em um grafo computacional.
result = sess.run(c)
print(result)  # 5

#tensorflow.summary : to save summary for tensorboard

#tensorflow.keras: TensorFlow's High-Level API for building and training models
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(64

#tensorflow.data: for loading, preprocessing and manipulating large dataset.
import tensorflow as tf

# Create a dataset from a CSV file
dataset = tf.data.experimental.make_csv_dataset(
    'path/to/data.csv',
    batch_size=32,
    label_name='label_column')

# Print the first element of the dataset
for feature, label in dataset.take(1):
    print("Example feature:", feature)
    print("Example label:", label)
