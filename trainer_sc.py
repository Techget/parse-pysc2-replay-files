from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.callbacks import TensorBoard
from keras.backend import image_dim_ordering
import pickle
import glob

EPOCHS = 2

input = Input(shape=(7, 60, 60))

compression = 16

x = Conv2D(compression*4, (3, 3), activation='relu', padding='same', name="enc_1")(input)
x = MaxPooling2D((2, 2), padding='same', name="enc_2")(x)
x = Conv2D(compression*2, (3, 3), activation='relu', padding='same', name="enc_3")(x)
x = MaxPooling2D((2, 2), padding='same', name="enc_4")(x)
x = Conv2D(compression, (3, 3), activation='relu', padding='same', name="enc_5")(x)
encoded = MaxPooling2D((2, 2), padding='same', name="encoded")(x)

x = Conv2D(compression, (3, 3), activation='relu', padding='same', name="dec_1")(encoded)
x = UpSampling2D((2, 2), name="dec_2")(x)
x = Conv2D(compression*2, (3, 3), activation='relu', padding='same', name="dec_3")(x)
x = UpSampling2D((2, 2), name="dec_4")(x)
x = Conv2D(compression*4, (3, 3), activation='relu', name="dec_5")(x)
x = UpSampling2D((2, 2), name="dec_6")(x)
decoded = Conv2D(7, (4, 4), activation='sigmoid', padding='same', name="decoded")(x)

autoencoder = Model(input, decoded)
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

# Load data
x_train = []
x_test = []

data_files = glob.glob("data/*")

n = len(data_files)
i = 0
for data_file in data_files:
    states = pickle.load(open(data_file, "rb"))
    if i > n * 0.75:
        x_test = x_test + states
    else:
        x_train = x_train + states
    i += 1

x_train = np.array(x_train).reshape((len(x_train), 7, 60, 60)).astype('float32')
x_test = np.array(x_test).reshape((len(x_test), 7, 60, 60)).astype('float32')

autoencoder.fit(x_train, x_train,
                epochs=EPOCHS,
                batch_size=128,
                shuffle=True,
                validation_data=(x_test, x_test),
                callbacks=[TensorBoard(log_dir='/tmp/autoencoder')])

autoencoder.save('autoencoder_' + str(EPOCHS) + '_32.h5')

print("Model saved")