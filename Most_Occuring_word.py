with open("/Users/rishu/CodePractice/python-practice/sample.txt", 'r') as f:
    lines = f.readlines()

    count = {}
    
for line in lines:
    words = line.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

max_word = ""
max_count = 0

for word in count:
    if count[word] > max_count:
        max_count = count[word]
        max_word = word

print(max_word, max_count)