names = ["Rishu", "Ayush", "Hitesh", "Mukul", "Rishabh"]

with open("/Users/rishu/CodePractice/python-practice/sample.txt", "w") as f:
    for name in names:
        f.write(name + "\n")