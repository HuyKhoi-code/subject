import glob
import numpy as np
import re
import os


# BUOC 1: Đọc file text trong thư mục 'data'
# va xay dung tap tu dien
# Lay danh sach file txt trong thu muc data
file_paths = glob.glob("C:/Users/Admin/Desktop/retrival/*.txt")
#print(txt_files)

# Doc noi dung cua tung file txt
# va xay dung tap "dictionary" chua danh sach cac tu
lst_contents = []
Name = []
dictionary = set()
for file_path in file_paths:
    f = open(file_path, 'r', encoding="utf-8")
    str = f.read()
    # lst_contents.append(str)
    words = str.replace('"', '').replace('.', '').replace("'","").split()
    Name.append(os.path.splitext(file_path)[0][9:])
    words = set(words)
    lst_contents.append(words)
    dictionary.update(words)
    #print(words)
    #print ('Noi dung file cua ban la:\n', str)
#print('Tap cac tu: ', dictionary)
dictionary = list(dictionary)

# BUOC 2: Xây dựng inverted file 
inv_files = dict()
for k,word in enumerate(dictionary):
    inv_files[word] = set()
    for i,content in enumerate(lst_contents):
        if word in content:
            inv_files[word].add(i)
#print(inv_files)

# BUOC 3: Nhập câu truy vấn và phân tách từ truy vấn
# phan tach tu trong van ban va cac tu logic
query = '"Man" AND "Madrid" XOR "chia"'
query_words = re.findall('"(\\w+)"', query)
logic_words = re.findall('(\\w+) ',query)

for i,word in enumerate(logic_words):
  if word in query_words : logic_words.pop(i)
print(query_words)
print(logic_words)

# BUOC 4: Tra từng từ trong inverted files 
# và kiểm tra văn bản nào có chứa nó
for query_word in query_words:
    # tra vi tri cua query_word trong dictionary
    try:
        file_name = inv_files[query_word]
        print('Tap hop van ban chua tu ', query_word, ' la: ', file_name)
    except:
        query_words.remove(query_word)

if not query_words:
    print ('ket qua rong')
    quit()
# BUOC 5: thực hiện phép biến đổi luận lý: AND, OR, XOR, NOT...
#tạo tập set gồm số lượng file
file_set = {i for i in range(len(file_paths))}
# thực hiện phép NOT
for i,word in enumerate(logic_words):
    if word=="NOT": 
        inv_files[query_words[i]]= file_set- inv_files[query_words[i]]
        logic_words.pop(i) 

result = inv_files[query_words[0]]
for i, word in enumerate(logic_words):
    if (word == "AND"):
        result = result & inv_files[query_words[i+1]]
    elif (word == "OR"):
        result = result | inv_files[query_words[i+1]]
    elif (word == "XOR"):
        result = result ^ inv_files[query_words[i+1]]
# BUOC 6: hiển thị kết quả sau khi biến đổi
print("cac file co chua ket qua",result)


