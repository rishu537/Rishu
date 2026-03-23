s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

sorted1 = sorted(s1)
sorted2 = sorted(s2)

if sorted1 == sorted2:
    print("The String are Anagram")
else:
    print("The String are not Anagram")