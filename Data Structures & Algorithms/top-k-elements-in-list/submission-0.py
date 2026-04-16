class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict = {}
        for el in nums:
            temp_dict[el] = temp_dict.get(el, 0) + 1
        top_k_items = heapq.nlargest(k, temp_dict.items(), key=lambda item: item[1])
        #print(top_k_items)
        return [item[0] for item in top_k_items]
        
        