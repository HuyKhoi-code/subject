import glob
import numpy as np
import re
import os


# BUOC 1: Đọc file text trong thư mục 'data'
# va xay dung tap tu dien
# Lay danh sach file txt trong thu muc data
file_paths = glob.glob("C:/Users/Admin/Desktop/boolean/*.txt")
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
# BUOC 2: Xây dựng ma trận term-document
term_doc = np.zeros((len(dictionary), len(file_paths)))
#print(term_doc)
#print('Kich thuoc ma tran: ', term_doc.shape)
for k,word in enumerate(dictionary):
    for i,content in enumerate(lst_contents):
        if word in content:
            term_doc[k,i] = 1
#print(term_doc)


# BUOC 3: Nhập câu truy vấn và phân tách từ truy vấn
query = '"Man" AND "Madrid" XOR "chia"'
query_words = re.findall('"(\\w+)"', query)
logic_words = re.findall('(\\w+) ',query)
#print(query_words)
query_arr = []
# BUOC 4: Tra từng từ trong ma trận term-document
# để lấy vector biểu diễn của từng từ
for query_word in query_words:
    # tra vi tri cua query_word trong dictionary
    try:
        k = dictionary.index(query_word)
        word_vec = term_doc[k,:]
        print('Vector bieu dien cua ', query_word, ' la: ', word_vec)
    except:
        word_vec = np.zeros (5)
    query_arr.append(word_vec)


# BUOC 5: thực hiện phép biến đổi luận lý: AND, OR, XOR, NOT...
# thuc hien phep NOT:
count = 0 
for i in range (len(logic_words)):
    if (logic_words[i] == 'NOT'):
        query_arr[i-count] = np.logical_not(query_arr[i-count])
        count+=1
#print (query_arr)
# loai bo NOT ra khoi query:
for i in range (len(logic_words)):
    if 'NOT' in logic_words:
        logic_words.remove('NOT')
#print (logic_words)
# thuc hien cac phep logic khac:
temp = query_arr[0]
for i in range (len(logic_words)):
    if (logic_words[i] == 'AND'):
        temp = np.logical_and(temp, query_arr[i+1])
    if (logic_words[i] == 'OR'):
        temp = np.logical_or(temp, query_arr[i+1])
    if (logic_words[i] == 'XOR'):
        temp = np.logical_xor(temp, query_arr[i+1])
temp = [1 if x==True else 0 for x in temp]
print (temp)

# BUOC 6: hiển thị kết quả sau khi biến đổi
for i in range(len(Name)):
  if temp[i] ==1:
    print('ket qua xuat hien o: ',Name[i])
