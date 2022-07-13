import csv
import os

# 2350자 리스트 생성
list_2350 = []
file_2350 = open("./2350-common-hangul.txt", "r")
while True:
    line = file_2350.readline()
    if not line:
        break
    list_2350.append(line.strip())

file_2350.close()

dir = './hangeul_image/out/'

files = os.listdir(dir)

print(len(files))
print(files[0][0])
print('퓸' in files[0])

# 파일 새로 작성
f = open("generated_data.csv", "w") 
f.close()

# 파일 쓰기
f = open("generated_data.csv", "a")
writer = csv.writer(f)

for file in files:
    if (os.path.isfile('./hangeul_image/out/' + file)):
        writer.writerow(['./hangeul_image/out/' + file, file[0]])
f.close()