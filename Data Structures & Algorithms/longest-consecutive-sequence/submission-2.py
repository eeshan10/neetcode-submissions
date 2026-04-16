class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for el in set_nums:
            if el-1 not in set_nums:
                max_length = 1  
                while (el + max_length) in set_nums:
                    max_length +=1
                longest = max(max_length, longest)
        return longest
        
        
        