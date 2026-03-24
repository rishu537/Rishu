# s = input("Enter a String: ")

# count = {}

# for char in s:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# for char in count:
#     print(char, "=", count[char])

s = input("Enter a String: ")

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

result = ""

for char in count:
    result += char + str(count[char])

print(result)