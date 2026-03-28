s = input("Enter a String: ")

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char in count:
    print(char, "=", count[char])
    