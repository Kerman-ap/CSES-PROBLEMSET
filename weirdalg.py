n = int(input())
nums = []
nums.append(str(n))
while n != 1:
    if n % 2:
        n = n * 3 + 1
    else:
        n = n // 2
    nums.append(str(n))
print(' '.join(nums))