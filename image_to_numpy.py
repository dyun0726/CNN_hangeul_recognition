import csv
import cv2
import numpy as np

img_size = 32
color = 1 # 흑백으로 학습하자

# 데이터 개수 확인
f = open("./resize_labels.csv", "r")
reader = csv.reader(f)
file_labels = list(reader)

f.close()
num_data = len(file_labels)
print(num_data)

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


x = np.zeros(num_data * img_size * img_size).reshape(num_data, img_size, img_size, color)
y = np.zeros(num_data)

print(x.shape)
print(y.shape)

i = 0
for file_label in file_labels:
    img = cv2.imread(file_label[0])
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_array= np.array(255 - img_gray).reshape(img_size, img_size, color)
    x[i] = img_array
    y[i] = labels.index(file_label[1])
    i += 1
    if (i % 10000 == 0):
        print("np convert proceed: " + str(i))

# print(x[-1]/255)
# print(y[-1])

np.save('./data_x_array', x)
np.save('./data_y_array', y)
print(labels[1471])

x = np.load('./data_x_array.npy')
y = np.load('./data_y_array.npy')

print(x[30]/255)
cv2.imwrite('./trf.jpg', x[30])
print(labels[int(y[30])])