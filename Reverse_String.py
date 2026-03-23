class StringOperation:

    def reverse_string(self, s):
        rev = ""

        for i in range(len(s) - 1, -1, -1):
            rev += s[i]

        return rev
    
obj = StringOperation()

s = input("Enter a String: ")
result = obj.reverse_string(s)

print("Reversed String ", result)