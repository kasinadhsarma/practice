class reverseInteger:
    def reverse(self,x:int)->int:
        # here the reversing integer formula is reversed_num = int(str(abs(x))[::-1])  * sign 
        # and then check for the 32-bit overflow
        # time complexity is O(1) - constant time complexity
        # space complexity is O(1) - constant space complexity
        # check if number is negative
        sign = -1 if x < 0 else 1
        # reversing the number
        reversed_num = int(str(abs(x))[::-1])  * sign 

        #32-bit overflow check
        if reversed_num < (-2**31) or reversed_num > (2**31 - 1):
            return 0
        return reversed_num

x = int(input("enter the number: "))
reverseInteger = reverseInteger()
print("the reversed number is: ",reverseInteger.reverse(x))
    