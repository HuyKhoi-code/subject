def checkOptimizeParition(arr, n):
    if n <=1:
        return False
    tong = sum(arr)
    if tong%2==1:
        return False
    
    part = [False for i in range(tong//2+1)]

    for i in range(n):
        for j in range(tong//2,arr[i]-1,-1):
            if j==arr[i] or part[j-arr[i]]==True:
                part[j] = True



    print(part)
    return part[tong//2]

arr = [1,2,1]
n = len(arr)
print(checkOptimizeParition(arr,n))