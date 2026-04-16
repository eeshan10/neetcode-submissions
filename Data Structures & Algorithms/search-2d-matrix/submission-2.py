class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #temp_dict = []
        for el in matrix:
            left = 0 
            right = len(el) -1 
            while left <= right:
                mid = (left +right)//2
                if el[mid] == target:
                    return True
                elif el[mid] < target:
                    left = mid +1 
                else:
                    right = mid -1 
        return False

        