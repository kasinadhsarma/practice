class pythogorentherom:
    # here pythogorentherom is a^2 + b^2 = c^2
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def get_pythogorentherom(self):
        return self.a * self.a + self.b * self.b


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
pythogorentherom = pythogorentherom(a,b)
print("the pythogorentherom is: ",pythogorentherom.get_pythogorentherom())