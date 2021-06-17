def checkPartition(arr, n):
    if n <= 1:
        return False
    tong = sum(arr)
    if tong%2!=0:
        return False
    
    part =[[True for i in range(n+1)] for j in range(tong//2+1)]

    for i in range(1, tong//2+1):
        part[i][0] = False

    for i in range(1,tong//2+1):
        for j in range(1, n+1):   
            part[i][j] = part[i][j-1]
            if i >= arr[j-1]:
                part[i][j] = part[i][j] or part[i-arr[j-1]][j-1]
    
    return part[tong//2][n]
    # for vec in part:
    #     print(vec)





arr = [1,2,2,1]
n = len(arr)
print(checkPartition(arr,n))