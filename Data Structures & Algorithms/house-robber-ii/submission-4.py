class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        
        firstHouse = [0] * len(nums)
        lastHouse = [0] * len(nums)

        firstHouse[0] = nums[0]
        firstHouse[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            firstHouse[i] = max(firstHouse[i-1], nums[i] + firstHouse[i-2])    

        for i in range(1, len(nums)):
            if i < 2:
                lastHouse[i] = nums[i]
                continue

            lastHouse[i] = max(lastHouse[i-1], nums[i] + lastHouse[i-2])



        firstMax = max(firstHouse[-1],firstHouse[-2])
        lastMax = max(lastHouse[-1],lastHouse[-2])


        return max(firstMax,lastMax)

        # if its second to last we can add first