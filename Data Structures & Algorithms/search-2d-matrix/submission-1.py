class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp_dict = []
        for el in matrix:
            temp_dict += el
            left = 0 
            right = len(temp_dict) -1 
            while left <= right:
                mid = (left +right)//2
                if temp_dict[mid] == target:
                    return True
                elif temp_dict[mid] < target:
                    left = mid +1 
                else:
                    right = mid -1 
        return False

        