class probability_of_event:
    # classical probability: favorable outcomes over total possible outcomes
    # time complexity O(1), space O(1)
    def calculate(self,favorable:int,total:int)->float:
        if total <= 0 or favorable < 0 or favorable > total:
            return None
        return favorable / total

favorable = 4   # e.g. drawing one of 4 aces
total = 52      # a standard deck
result = probability_of_event().calculate(favorable, total)
print(result)
