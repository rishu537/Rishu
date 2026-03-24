s = input("Enter a sentence: ")

split = s.split()
result = []

for char in split:
    result.append(char[::-1])

output = " ".join(result)
print(output)
