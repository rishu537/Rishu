with open("sample.txt", "r") as f:
    data = f.readlines()

    fifth_lines = data[4]

    words = fifth_lines.split()

    print(words[4])


