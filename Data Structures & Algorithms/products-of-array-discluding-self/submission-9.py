class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)

        # get prefixes
        compound = 1
        for i in range(1, len(nums)): 
            compound *= nums[i-1]
            prefix[i] = compound
        # get suffixes
        compound = 1
        for i in range(len(nums) - 2, -1, -1):
            compound *= nums[i+1]
            suffix[i] = compound

        # get product except self
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output