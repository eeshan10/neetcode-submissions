import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1 
        while left<= right :
            print(left, right)
            mid = (left +right)//2
            print(mid) 
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            if total_hours <= h:
                right = mid - 1
            else:
                left = mid +1
        return left