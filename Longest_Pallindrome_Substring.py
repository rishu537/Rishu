s = input("Enter the String: ")

longest = ""

for i in range(len(s)):
    for j in range(i+1, len(s)):
        substring = s[i:j+1]
        if substring == substring[::-1]:
            if len(s) > len(longest):
                longest = substring

print(longest)
