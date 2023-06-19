class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for x in bills:
            if x == 5:
                five += 1
            elif x == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            else:  # 20
                if ten >= 1 and five >= 1:
                    ten -= 1  # ten first
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True