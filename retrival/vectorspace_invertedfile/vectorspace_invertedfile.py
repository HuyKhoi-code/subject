import glob
import numpy as np
import re

def load_data_in_a_directory(data_path):
    file_paths = glob.glob(data_path)
    lst_contents = []
    for file_path in file_paths:
        f = open(file_path, 'r', encoding='utf-8')
        str = f.read()
        words = str.replace('"', '').replace('.', '').replace("'","").split()
        #words = set(words)
        lst_contents.append(words)
    return (lst_contents, file_paths)

def build_dictionary(contents):
    dictionary = set()
    for content in contents:
        dictionary.update(content)
    return dictionary

contents, paths = load_data_in_a_directory('C:/Users/Admin/Desktop/vectorspace_invertedfile/test_data/*.txt')
vocab = build_dictionary(contents)

inv_files = dict()
IDF = dict()
for k,word in enumerate(vocab):
    inv_files[word] = np.array([])
    IDF[word] = list()
    count = 0
    for i,content in enumerate(contents):
        if word in content:
            inv_files[word] = np.append(inv_files[word],i)
            inv_files[word] = np.append(inv_files[word],content.count(word)/len(content))
            count+=1
    IDF_ = 1 +np.log(len(contents)/count)
    inv_files[word][1::2]=inv_files[word][1::2]*IDF_
    inv_files[word] = list(inv_files[word])
    IDF[word].append(IDF_)
#print(inv_files)

def calc_tf_weighting_query(vocab, contents):
  inv_files_query = dict()
  #print(vocab)
  for k,word in enumerate(vocab):
      inv_files_query[word] = list()
      count = 0
      for i,content in enumerate(contents):
          if word in content:
              #inv_files_query[word].append(i)
              inv_files_query[word].append(content.count(word)/len(content))
              count+=1
  return inv_files_query

def calc_tfidf_weighting_query(inv_files_query, IDF):
    for word in vocab:
      try:
        inv_files_query[word] = np.dot(inv_files_query[word],IDF[word])
      except:
        pass
        inv_files_query[word] = 0
    return inv_files_query

query="Trump"
qcontent = query.split()
inv_files_query = calc_tf_weighting_query(vocab, [qcontent])
inv_files_query = calc_tfidf_weighting_query(inv_files_query, IDF)
#inv_files_query

rank = list()
for i in range(len(contents)):
  distance = 0
  for word in vocab:
    if (i in inv_files[word] and inv_files[word].index(i)%2==0) and inv_files_query[word]==0:
      distance += inv_files[word][inv_files[word].index(i)+1]**2
    elif (i in inv_files[word] and inv_files[word].index(i)%2==0) and inv_files_query[word]!=0:
      distance += (inv_files[word][inv_files[word].index(i)+1]-inv_files_query[word])**2
    else: 
      distance += inv_files_query[word]**2
  rank.append(np.sqrt(distance))

rank = np.argsort(rank)
print(rank)
topK = 4
for i in range(topK):
    print('Van ban gan thu ', i+1, ' la: ', ' '.join(contents[rank[i]]))