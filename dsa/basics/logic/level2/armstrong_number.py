class armstrong:
    # here forumula is N = (d1)^k + (d2)^k + (d3)^k + ... + (dn)^k 
    # here time complexity is O(1) - constant time complexity
    # here space complexity is O(1) - constant space complexity
    
    def __init__(self, N):
        self.N = N
    def get_armstrong(self):
        temp = self.N
        k = len(str(self.N))
        sum_of_powers = 0
        while temp > 0:
            digit = temp % 10
            sum_of_powers += digit ** k
            temp //= 10
        return sum_of_powers == self.N

N = int(input("enter the number: "))
armstrong = armstrong(N)
print("the armstrong number is: ",armstrong.get_armstrong())
