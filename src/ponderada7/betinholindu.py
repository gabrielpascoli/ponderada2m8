#! /bin/env python3
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train = tf.keras.utils.normalize(x_train, axis=1)
    x_test = tf.keras.utils.normalize(x_test, axis=1)
    
    model_name = 'betinholindu.model'

    model = tf.keras.models.Sequential() 
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    model.fit(x_train, y_train, epochs=3)

    val_loss, val_acc = model.evaluate(x_test, y_test)
    print(f"Model Losses: {val_loss}")
    print(f"Model Accuracy: {val_acc}")

    model.save(model_name)

    betinholindu = tf.keras.models.load_model(model_name)
    predictions = betinholindu.predict([x_test])
    print(np.argmax(predictions[0]))
    plt.imshow(x_test[0])
    plt.show()

if __name__ == "_main_":
    main()