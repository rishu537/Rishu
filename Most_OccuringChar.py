s = input("Enter a String: ")

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max_char = ""
max_count = 0 

for char in count:
    if count[char] > max_count:
        max_count = count[char]
        max_char = char

print(max_char, "=", max_count)
    