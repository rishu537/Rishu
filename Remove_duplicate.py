s = input("Enter a String: ")

seen = set()
result = ""

for char in s:
    if char not in seen:
        seen.add(char)
        result += char

print(result)