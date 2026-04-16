class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i , len(heights)):
                print(i,j, heights[i:j +1])
                area = min(heights[i:j +1])*(j - i +1)
                print(area)
                if area>max_area:
                    max_area = area
        return max_area

        