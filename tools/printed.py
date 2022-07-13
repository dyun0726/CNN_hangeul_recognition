import json
import csv
import os
file = json.load(open('./hangeul_image/printed/printed_data_info.json'))

# 2350자 리스트 생성
list_2350 = []
file_2350 = open("./2350-common-hangul.txt", "r")
while True:
    line = file_2350.readline()
    if not line:
        break
    list_2350.append(line.strip())

file_2350.close()

syllables_anno = [f for f in file['annotations'] if f['attributes']['type']=='글자(음절)']
print(syllables_anno[:3])
print(len(syllables_anno))

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
#     if (os.path.isfile('./hangeul_image/printed/syllable/' + s)):
#         os.remove('./hangeul_image/printed/syllable/' + s)
#         num += 1
# print(num) # 확인 코드

# 파일 새로 작성
f = open("printed_data.csv", "w") 
f.close()

# 파일 쓰기
f = open("printed_data.csv", "a")
writer = csv.writer(f)

for i in range(len(syllables_2350_file_name)):
    if (os.path.isfile('./hangeul_image/printed/syllable/' + syllables_2350_file_name[i])):
        writer.writerow(['./hangeul_image/printed/syllable/' + syllables_2350_file_name[i], text_syllables[i]])
f.close()