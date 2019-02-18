import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.datasets import mnist
import keras.optimizers as optimizers

import tensorflow as tf

config = tf.ConfigProto(intra_op_parallelism_threads=1,\
                        inter_op_parallelism_threads=1,\
                        allow_soft_placement=True,\
                        device_count = {'CPU': 1})
session = tf.Session(config=config)

batch_size = 32
num_classes = 10
epochs = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train[:50000,:,:]
y_train = y_train[:50000]

x_train = x_train.reshape(50000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential([
    Dense(30, input_shape=(784,)),
    Activation('sigmoid'),
    Dense(10),
    Activation('sigmoid'),
])

sgd = optimizers.SGD(lr=3.)
model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=2,
                    validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=1)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
