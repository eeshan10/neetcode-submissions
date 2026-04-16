class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #heights = sorted(heights)
        left = 0
        right = len(heights) -1
        max_area = 0
        while left< right:
            # print("left side is", left, heights[left])
            # print("right side is", right, heights[right])
            temp_area = (right- left)*min(heights[left], heights[right])
            #print("area is", temp_area)
            if temp_area > max_area:
                max_area = temp_area
            if min(heights[left], heights[right]) == heights[left]:
                left +=1 
            elif min(heights[left], heights[right]) == heights[right]:
                right -=1
        return max_area

        