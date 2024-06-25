n = int(input())
nlist = input().split()
nlist = [int(x) for x in nlist]

listsum = sum(nlist)

estsum = n * (n + 1) // 2

print(round(estsum - listsum))