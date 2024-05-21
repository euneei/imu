import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

df = pd.read_csv('data221(walk,run,oth).csv')
df = df.drop('SVMacc', axis=1)

X = df.drop('y_class', axis=1).values

X_train, X_val, y_train, y_val = train_test_split(df.iloc[:, 1:], df.iloc[:, 0], test_size=0.2, shuffle=True, random_state=42)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv1D(filters = 16, kernel_size = 3, activation = 'relu',input_shape = (300,1)))
model.add(tf.keras.layers.Conv1D(filters = 8 , kernel_size = 5,activation='relu'))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(4,activation='softmax'))
model.compile(loss = 'sparse_categorical_crossentropy', optimizer='ADAM', metrics = ["accuracy"])
model.summary()
model.fit(X_train, y_train, epochs=50,batch_size = 10,
                    validation_data=(X_val, y_val))

model.save('traincnn.h5')