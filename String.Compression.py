s = input("Enter a String: ")

current_char = s[0]
count = 0
result = ""

for char in range(1, len(s)):
    if s[char] == current_char:
        count += 1
    else:
        result += current_char + str(count)
        current_char = s[char]
        count = 1

result += current_char + str(count)
print(result)