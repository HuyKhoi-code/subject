import random

shape = 4

img = [[random.randint(0,5) for i in range (shape)] for j in range (shape)]


def Create_cost (img, shape):
    cmap = img
    path = [[0 for i in range (shape)] for j in range (shape)]
    for i in range (1, shape):
        for j in range (shape):
            if (j == 0):
                cmap[i][j] = img[i][j] + min(cmap[i-1][j], cmap[i-1][j+1])
                path[i][j] = cmap[i-1][j:j+2].index(min(cmap[i-1][j], cmap[i-1][j+1]))


            elif (j == shape -1):
                cmap[i][j] = img[i][j] + min(cmap[i-1][j-1],cmap[i-1][j])
                path[i][j] = cmap[i-1][j-1:j+1].index(min(cmap[i-1][j-1],cmap[i-1][j]))+j-1
                
            else:
                cmap[i][j] = img[i][j] + min(cmap[i-1][j-1],cmap[i-1][j], cmap[i-1][j+1])
                path[i][j] = cmap[i-1][j-1:j+2].index(min(cmap[i-1][j-1],cmap[i-1][j], cmap[i-1][j+1]))+j-1
                

    return cmap,path

def trace_back (cmap, path, img):

    cur_point = cmap[shape-1].index(min(cmap[shape-1]))
    index_path = []
    
    index_path.append(path[shape-1][cur_point])

    cur_row = shape-1
    while cur_row > 0:
        print('cur point:', cur_point)
        index_path.append(path[cur_row][cur_point])
        cur_point = path[cur_row-1][cur_point]
        cur_row-=1

    seam = []
    for i in range (len(index_path)):
        seam.append((i,index_path[i]))
    return seam

        
for r in img:
    print (*r)
    

print ("__________________")

result, path = Create_cost(img,shape)
t = trace_back(result, path, img)
for r in result:
    print (*r)

print ("_________________")

for r in path:
    print (*r)

print ("_________________")

for r in t:
    print (r)


                