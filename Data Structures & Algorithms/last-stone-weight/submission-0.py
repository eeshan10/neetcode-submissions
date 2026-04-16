import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -1*heapq.heappop(stones)
            y = -1*heapq.heappop(stones)
            if x > y:
                rem_el = x - y
                heapq.heappush(stones, -1*rem_el)
        stones.append(0)
        return abs(stones[0])
        
            



        