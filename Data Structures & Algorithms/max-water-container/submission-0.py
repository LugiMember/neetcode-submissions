class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #from each side:
        # pick the first column and iterate
        #   while iterating if a column is higher 
                # check if its area is larger if larger replace
        
        res = 0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j-i))
        return res        