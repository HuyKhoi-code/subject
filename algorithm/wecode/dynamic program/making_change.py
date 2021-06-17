# Given an integer representing a given amount of change, write a
# function to compute the total number of coins required to make
# that amount of change. You can assume that there is always a
# 1¢ coin.
# eg. (assuming American coins: 1, 5, 10, and 25 cents)
# makeChange(1) = 1 (1)
# makeChange(6) = 2 (5 + 1)
# makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)

def change(coins, num):
    memoi = [0] * (num+1)
    for i in range (2, num+1):
        if (i in coins):
            memoi[i] = 1
        else:
            dp = [memoi[i-c] for c in coins]
            dp = [i for i in dp if i > 0]
            if (len(dp) == 0):
                memoi[i] == 0
            else:
                memoi[i] = min(dp) + 1
    return memoi[num]

def change2 (coins, num):
    memoi = [0] * (num +1)
    memoi[0] = 0
    for i in range (num+1):
        memoi[i] = min(memoi[num-c] for c in coins if c < num)+1
    return memoi[num]
coins = [1,6, 10]
num = 8
print (change2(coins, num))
