def checkPartition(arr, n):
    if n <= 1:
        return False, None
    tong = sum(arr)
    if tong%2!=0:
        return False, None
    
    part =[[True for i in range(n+1)] for j in range(tong//2+1)]

    for i in range(1, tong//2+1):
        part[i][0] = False

    for i in range(1,tong//2+1):
        for j in range(1, n+1):   
            part[i][j] = part[i][j-1]
            if i >= arr[j-1]:
                part[i][j] = part[i][j] or part[i-arr[j-1]][j-1]
    
    for i in part:
        print(i)
    return part[tong//2][n],part
    # for vec in part:
    #     print(vec)


def trace_back(part, s, arr):
    tong = 0
    index = len(part)-1
    path = []

   # i = part[index].index(True)
    while tong != s:
        #print('index:',index)
        i=part[index].index(True) - 1
        #print('i:', i)
        #print('A[i]:', arr[i])
        tong+=arr[i]
        path.append(i)
        index = index - arr[i]
    
    s1 = []
    s2 = []
    for i in range(len(arr)):
        if i in path:
            s1.append(arr[i])
        else:
            s2.append(arr[i])
    return s1,s2
        







arr = [0]
n = len(arr)
result, part = checkPartition(arr, n)
if result==True:
    s1,s2 = trace_back(part,sum(arr)//2, arr) 
    print("subset 1:", s1)
    print("subset 2:", s2)
#print(checkPartition(arr,n))