sequence = input()

prevletter = None
longest = 0
currentlength = 0
for letter in sequence:
    if letter != prevletter:
        prevletter = letter
        currentlength = 1
    else:
        currentlength += 1
    if currentlength > longest:
        longest = currentlength
print(longest)