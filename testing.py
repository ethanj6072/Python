def print2DArray(n):
    string = ""
    for f in range(10):
        for d in range(10):
            string += str(n[f][d]) + " "
        print(string)
        string = ""

def findSum(list):
    total = 0
    for sublist in list:
        total += sum(sublist)
        
    print (str(total))


import math
import random

nums = []

for i in range(10):
    nums.append([])
    for j in range(10):
        nums[i].append(math.floor(random.random()*10))

print2DArray(nums)
findSum(nums)