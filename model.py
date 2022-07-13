import tensorflow as tf
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

# 그래픽 카드 설정
os.environ["CUDA_VISIBLE_DEVICES"]='0' 

x = np.load('./data_x_array.npy')
y = np.load('./data_y_array.npy')

x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, shuffle=True, stratify=y, random_state=34)

# print(x_train.shape)
# print(x_valid.shape)
# print(y_train.shape)
# print(y_valid.shape)

cv2.imwrite('./example.jpg', x_train[100])
print(y_train[100])
cv2.imwrite('./example2.jpg', x_train[101])
print(y_train[101])

x_train, x_valid = x_train / 255, x_valid / 255

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(64, (3, 3), padding = 'same', activation = 'relu', input_shape = (32, 32, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(128, (3, 3), padding = 'same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(256, (3, 3), padding = 'same', activation='relu'))
model.add(tf.keras.layers.Conv2D(256, (3, 3), padding = 'same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(512, (3, 3), padding = 'same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Conv2D(512, (3, 3), padding = 'same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(2350, activation='softmax'))

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

epoch = 25
batch = 32

hist = model.fit(x_train, y_train, batch_size = batch, epochs = epoch, verbose = 1, validation_data=(x_valid, y_valid))

model.evaluate(x_valid, y_valid, verbose = 1)

model.save('./model/'+ str(epoch) + '_' + str(batch) + '_2.h5')

# 학습 과정 그림 그리기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.savefig('./model_graph/'+ str(epoch) + '_' + str(batch) + '_train_hist_2.png')