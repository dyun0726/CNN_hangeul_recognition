import json
import csv
import os
file = json.load(open('./hangeul_image/handwriting/handwriting_data_info_clean.json'))

# print(file.keys()) #dict_keys(['info', 'images', 'annotations', 'licenses'])
# print(file['info']) #{'name': 'Text in the wild Dataset', 'date_created': '2019-10-14 04:31:48'}
# print(type(file['images'])) #list
# print(file['annotations'][0])
# print(file['annotations'][0]['attributes']['type'] == '글자(음절)')

# import matplotlib.image as img
# import matplotlib.pyplot as pp
# 이미지 출력
# ndarray = img.imread(fileName)
# pp.imshow(ndarray)
# pp.show()

list_2350 = []
file_2350 = open("./2350-common-hangul.txt", "r")
while True:
    line = file_2350.readline()
    if not line:
        break
    list_2350.append(line.strip())

file_2350.close()
# print(list_2350)

# 음절인 것들만 뽑아서 리스트 만들기
syllables_anno = [f for f in file['annotations'] if f['attributes']['type']=='글자(음절)']

not_syllables_2350_file_name = []
syllables_2350_file_name = []
text_syllables = []
for syl in syllables_anno:
    if syl['text'] not in list_2350:
        not_syllables_2350_file_name.append(syl['image_id'] + '.png')
    else:
        syllables_2350_file_name.append(syl['image_id'] + '.png')
        text_syllables.append(syl['text'])

print(syllables_2350_file_name[:10])
print(text_syllables[:10])
print(len(syllables_2350_file_name))

# 필요없는 데이터 지우는 과정
# num = 0
# for s in not_syllables_2350_file_name:
#     if (os.path.isfile('./hangeul_image/handwriting/' + s)):
#         os.remove('./hangeul_image/handwriting/' + s)
#         num += 1
# print(num) # 확인 코드

# 파일 새로 작성
f = open("handwriting_data.csv", "w") 
f.close()

# 파일 쓰기
f = open("handwriting_data.csv", "a")
writer = csv.writer(f)

for i in range(len(syllables_2350_file_name)):
    writer.writerow(['./hangeul_image/handwriting/' + syllables_2350_file_name[i], text_syllables[i]])
f.close()

fileName = "./hangeul_image/handwriting/" + syllables_2350_file_name[0]
print(fileName)
