'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def partition(arrToSort, low, high):
    i = (low-1)         # index of smaller element
    pivot = arrToSort[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if int(arrToSort[j]) <= int(pivot):
  
            # increment index of smaller element
            i = i+1
            arrToSort[i], arrToSort[j] = arrToSort[j], arrToSort[i]
    arrToSort[i+1], arrToSort[high] = arrToSort[high], arrToSort[i+1]
    return (i+1)
  
# arrToSort[] is array to be sorted,
# low is starting index,
# high is ending index
  
# Function to do Quick sort
def quickSort(arrToSort, low, high):
    if len(arrToSort) == 1:
        return arrToSort
    if low < high:
  
        # pi is partitioning index, arrToSort[p] is now
        # at right place
        pi = partition(arrToSort, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arrToSort, low, pi-1)
        quickSort(arrToSort, pi+1, high)

def binSearch(arr, x):
    low = 0
    mid = 0
    high = len(arr) - 1
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # otherwise x is present at mid
        else:
            return mid
 
    # fail case
    return -1

# Write your code here
numLines = input()
lines = input().split(" ")
lines = list(map(int, lines))

#sort in order
queriesNum = input()
for i in range(int(queriesNum)):
    currentInput = input().split(" ") #important! direct index-based solutions don't work on 2-digit nums
    pointValue = int(currentInput[0]) + int(currentInput[1])
    currentSet = lines.copy()
    currentSet.append(pointValue)
    quickSort(currentSet, 0, len(currentSet) - 1)

    # and now, because I'm supposed to demonstrate understanding of binary search
    numBetween = binSearch(currentSet, pointValue)
    print(numBetween)