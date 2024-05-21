import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

df = pd.read_csv('data221(walk,run,oth).csv')
df = df.drop('SVMacc', axis=1)

X = df.drop('y_class', axis=1).values

fs = 50  # 샘플링 주파수

# 데이터 X에 대해 각 행별로 FFT 실행
fft_values = np.fft.fft(X, axis=1)  
fft_freq = np.fft.fftfreq(X.shape[1], 1/fs)  
pos_indices = fft_freq > 0
magnitudes = np.abs(fft_values[:, pos_indices]) / X.shape[1]

X_train, X_val, y_train, y_val = train_test_split(magnitudes, df.iloc[:, 0].astype(int), test_size=0.2, shuffle=True, random_state=42)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv1D(filters = 16, kernel_size = 3, activation = 'relu',input_shape = (149,1)))
model.add(tf.keras.layers.Conv1D(filters = 8 , kernel_size = 5,activation='relu'))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(4,activation='softmax'))
model.compile(loss = 'sparse_categorical_crossentropy', optimizer='ADAM', metrics = ["accuracy"])
model.summary()
model.fit(X_train, y_train, epochs=50,batch_size = 10,
                    validation_data=(X_val, y_val))

# model.save('trainfftcnn.h5')