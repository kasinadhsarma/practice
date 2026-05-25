class leapyear:
    # find whether the year is leap year or not
    # here formula is in mathmatical mode is  year % 4 == 0
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, year):
        self.year = year
    def get_leapyear(self):
        return "leap year" if self.year % 4 == 0 else "not a leap year"


year = int(input("enter the year: "))
leapyear = leapyear(year)
print("the year is: ",leapyear.get_leapyear())