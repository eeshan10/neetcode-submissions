class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_list = []
        cntr = 0
        for el in nums:
            if el in final_list:
                cntr = cntr + 1
            else:
                final_list.append(el)
        if cntr > 0:
            return True 
        elif cntr == 0:
            return False
       
        