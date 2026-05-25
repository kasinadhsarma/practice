class even_odd:
    # numerically check the number is even or odd 
    # here mathematically formula of even or odd is num % 2 == 0
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, num):
        self.num = num
    def get_even_odd(self):
        return "even" if self.num % 2 == 0 else "odd"


num = int(input("enter the number: "))
even_odd = even_odd(num)
print("the number is: ",even_odd.get_even_odd())