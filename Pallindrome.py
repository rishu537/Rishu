class StringOperation:

    def pallindrome(self, s):
        n = len(s)

        for i in range(n):
            if s[i] != s[n - 1 - i]: 
                return "Not Pallindrome"
            
        return "Pallindrome"
    
obj = StringOperation()

s = input("Enter a String: ")
result = obj.pallindrome(s)

print(result)