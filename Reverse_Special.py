s = input("Enter a String: ")

letter = []

for char in s:
    if char.isalpha():
        letter.append(char)

letter.reverse()

result = []

letter_index = 0

for char in s:
    if char.isalpha():
        result.append(letter[letter_index])
        letter_index += 1
    else:
        result.append(char)

output = "".join(result)
print(output)
