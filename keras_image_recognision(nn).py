# -*- coding: utf-8 -*-
"""Keras image recognision(NN)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6LO9gyvrOzjGlVkRzCtS3fZQ1xLgoFi

Digit Recognition
"""

!pip install mnist

import keras
import tensorflow
import mnist

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images  = mnist.test_images()
test_labels  = mnist.test_labels()

type(train_images)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
first_image = train_images[199]
plt.imshow(first_image,cmap="gray")
plt.show()

"""### What is the ratio b/w train and test data here?
  6/7 is training and 1/7 is testing
"""

train_images.shape

test_images.shape

# Normalize the images

train_images = (train_images/255)
test_images = (test_images/255)

# Flatten the images

train_images = train_images.reshape((-1,784))
test_images = test_images.reshape((-1,784))

# Build the model

model = Sequential([
  Dense(64, activation='relu',input_shape = (784,)),
  Dense(64, activation= 'relu'),
  Dense(10, activation='softmax'),
])

# Compile the model

model.compile(
  optimizer='adam',
  loss='categorical_crossentropy',
  metrics = ['accuracy']
)

model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=7,
    batch_size=32
)

train_images[0]

# Evaluate the model

model.evaluate(
    test_images,
    to_categorical(test_labels)
               )

test_images[44].reshape((28,28))

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
first_image = train_images[44]
plt.imshow(first_image.reshape((28,28)), cmap ='gray')
plt.show()

np.argmax(model.predict(test_images[44].reshape((-1,784))))

#Predict on the first 5 test images
predictions = model.predict(test_images[:5])

#Print the model's preductions.
print(np.argmax(predictions, axis=1))

#Check our predictions against the ground truths.
print(test_labels[:5])

