s = input("Enter a String: ")

def permutation(s):
    if len(s) == 1:
        return [s]
    
    result = []

    for i in range(len(s)):
        current_char = s[i]
        remaining = s[:i] + s[i+1:]

        for perms in permutation(remaining):
            result.append(current_char + perms)

    return result

all_perms = permutation(s)

for perms in all_perms:
    print(perms)