s = input("Enter a String: ")

set = set()
result = ""

for char in s:
    if char not in set:
        set.add(char)
        result += char

print(result)
