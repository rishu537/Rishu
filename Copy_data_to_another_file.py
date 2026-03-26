with open ("/Users/rishu/CodePractice/python-practice/sample.txt", "r") as f:
    line = f.read()


with open("/Users/rishu/CodePractice/python-practice/demo.txt", "w") as f:
    f.write(line)
    
print("Successfull")