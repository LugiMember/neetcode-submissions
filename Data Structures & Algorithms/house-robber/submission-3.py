class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        moneys = [0] * len(nums)
        for i in range(len(nums)):
            if i < 1:
                moneys[i] = nums[i]
                continue
            
            moneys[i] = max(moneys[i-1], nums[i] + moneys[i-2])

        print(moneys)
        return max(moneys[-1], moneys[-2])




# at 1 just 1
# at 2 its 0 and 2
# at 3 its whether 0 and 3 is greater than 1 and 3
