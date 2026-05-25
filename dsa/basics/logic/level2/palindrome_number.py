class palindrome:
    # checking palindrome check either number or not yet 
    # here mathematically formula of palindrome is num == num_re
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, num):
        self.num = num
        temp = num
        self.num_re = 0
        while temp > 0:
            self.num_re = self.num_re * 10 + temp % 10
            temp //= 10
    def get_palindrome(self):
        return "palindrome" if self.num == self.num_re else "not a palindrome"


num = int(input("enter the number: "))
palindrome = palindrome(num)
print("the number is: ",palindrome.get_palindrome())