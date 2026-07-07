import math

class trig_ratios:
    # the three primary ratios in a right triangle, relative to a chosen angle:
    #   sin = opposite / hypotenuse
    #   cos = adjacent / hypotenuse
    #   tan = opposite / adjacent
    # time complexity O(1), space O(1)
    def sin(self,opposite:float,hypotenuse:float)->float:
        return opposite / hypotenuse

    def cos(self,adjacent:float,hypotenuse:float)->float:
        return adjacent / hypotenuse

    def tan(self,opposite:float,adjacent:float)->float:
        return opposite / adjacent

    def angle_from_sides(self,opposite:float,adjacent:float)->float:
        # inverse tangent gives the angle back, in degrees
        return math.degrees(math.atan2(opposite, adjacent))

opposite, adjacent, hypotenuse = 3, 4, 5
tr = trig_ratios()
result = (tr.sin(opposite, hypotenuse), tr.cos(adjacent, hypotenuse), tr.tan(opposite, adjacent))
print(result)
