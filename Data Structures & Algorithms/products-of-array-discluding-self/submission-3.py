class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #get product 
        if 0 not in nums:
            pr = 1 
            for el in nums:
                pr = pr*el
            final_list = []
            for el in nums:
                final_list.append(int(pr/el))
        elif 0 in nums:
            
            temp_list = nums.copy()
            temp_list.remove(0)
            final_list = [0]*len(nums)
            pr = 1
            for el in temp_list:
                pr = pr*el
            final_list[nums.index(0)] = pr
        return final_list
        