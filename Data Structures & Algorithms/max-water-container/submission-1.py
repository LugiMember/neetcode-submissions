class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #from each side:
        # pick the first column and iterate
        #   while iterating if a column is higher 
                # check if its area is larger if larger replace
        
        l, r = 0, len(heights) -1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)   
            res = max(res, area)
            if heights [l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res