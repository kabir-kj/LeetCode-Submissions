class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        add =0
        maxx =0
        for i in gain:
            add+= i
            maxx= max(add,maxx)
        return maxx