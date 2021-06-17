import random

def findPartition(arr, n):
    if n<=1:
        return False
    count = 0
    sum = 0
    # calculate sum of all elements
    
    count += 1 # khoi tao i
    for i in range(n):
        count+=2 # dieu kien dung, i++    for(int i=0li<n;i++)
        sum += arr[i]
        count +=1  # sum+=
    
    count +=2 # sum%2, !=0
    if sum % 2 != 0:
        return False
    
    
    
    part = [[True for i in range(n + 1)] for j in range(sum // 2 + 1)]
    ##    
    count += 1 # khoi tao i    for (int i=0;i<n+1;i++)

    # for i in range(n+1):
    count+=2*(n+1) # dieu kien dung, i++ 
    count+=1*(n+1) # khoi tao j
    count+=1*(n+1) # n+1
    #     for j in range(sum // 2 + 1):
    count+=2*(sum // 2 + 1)*(n+1) # dieu kien dung, i++ 
    count+=2*(sum // 2 + 1)*(n+1) # sum//2+1
    #         part[i][j] = True
    count+=1*(sum // 2 + 1)*(n+1) # =
    # initialize top row as true
    count+=1   # khoi tao i
    for i in range(n + 1):
        count+=2 # dieu kien dung, i++
        count+1 # n+1
        count+=1 # =
        part[0][i] = True
    
    # ineftmost column,
    # except part[itialize l0][0], as 0
    count+=1 # khoi tao i
    for i in range(1, sum // 2 + 1):
        count+=2 # dieu kien dung, i++ 
        count+=2 # sum // 2 + 1
        count+=1 # =
        part[i][0] = False



    # fill the partition table in
    # # bottom up manner
    count+=1 # khoi tao i
    for i in range(1, sum // 2 + 1):
        count += 2 # dieu kien dung + i++
        count += 2 # sum//2+1
        count += 1 # khoi tao j
        for j in range(1, n + 1):
            count +=2 # dieu kien dung + j++
            count +=1 # n+1
            part[i][j] = part[i][j - 1]
            count += 1 # j-1
            count +=1 # =
            if i >= arr[j - 1]:
                count += 1 # >=
                count+=1 # j-1
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
                count += 1 # =
                count += 1 # or
                count+=3 # - - - 
    
    print(count)

                          
    # for row in part:
    #     print(row)
    return part[sum // 2][n]
    #return count


# Driver Code
arr = [3,1,2,2,2]
n = len(arr)
# length_start = 0
# length_arr = 10
# for i in range(20):
#     arr = random.sample(range(0, length_start+1000), length_arr)
#     print(len(arr),sum(arr))
#     length_start+=1000
#     length_arr = int(length_arr*1.45)
#     print(findPartition(arr, len(arr)))



# Function call
print(findPartition(arr, n))

