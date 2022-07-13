import tensorflow as tf
import os
import cv2
import numpy as np

# 라벨 만들기
labels = []
f = open("./2350-common-hangul.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    labels.append(line.strip())
f.close()
print(len(labels))

os.environ["CUDA_VISIBLE_DEVICES"]='0' 

model = tf.keras.models.load_model('./model/25_32.h5')

img = cv2.imread('./test_image/hangul_sample5.jpeg')
img = cv2.resize(img, (32, 32))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
# 검정색이랑 하얀색 바꾸는 코드
# img_gray = 255- img_gray

img_array = np.array(img_gray / 255).reshape(1, 32, 32, 1)

# print(img_array.shape)

predictions = model.predict(img_array).squeeze()
print(np.sum(predictions))

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(labels[np.argmax(predictions)], 100 * np.max(predictions))
)


sort_index = predictions.argsort()[::-1]

print("Top 5 classify")
print(labels[sort_index[0]] + ': ' + str(predictions[sort_index[0]]*100))
print(labels[sort_index[1]] + ': ' + str(predictions[sort_index[1]]*100))
print(labels[sort_index[2]] + ': ' + str(predictions[sort_index[2]]*100))
print(labels[sort_index[3]] + ': ' + str(predictions[sort_index[3]]*100))
print(labels[sort_index[4]] + ': ' + str(predictions[sort_index[4]]*100))

# print(predictions[0])