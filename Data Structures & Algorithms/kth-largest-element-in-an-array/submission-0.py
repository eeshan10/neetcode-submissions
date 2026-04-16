import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k >0 :
            el_ret = heapq.heappop(nums)
            k = k-1
        return -1*el_ret

        