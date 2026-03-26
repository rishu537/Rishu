with open ("/Users/rishu/CodePractice/python-practice/demo.txt", "r") as f:

    data = f.readlines()
seen = set()
result = []

for line in data:
    words = line.split()
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
print(" ".join, result)
