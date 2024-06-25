n = int(input())
arr = [int(x) for x in input().split()] 

totalsum = 0
prevnum = arr[0]
for index, num in enumerate(arr):
    if prevnum > num:
        totalsum += prevnum - num
    else:  
        prevnum = num

print(totalsum)