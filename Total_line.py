with open("/Users/rishu/CodePractice/python-practice/sample.txt", "r") as f:
    data = f.readlines()

    total_words = 0

    for line in data:
        words = line.split()
        total_words += len(words)

    print(total_words)