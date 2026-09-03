class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) -1
        Area = 0
        while not i == j:
            width = j -i
            height = min(heights[i], heights[j])
            tempArea = width * height
            Area = max(tempArea,Area)
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                j -= 1

        return Area