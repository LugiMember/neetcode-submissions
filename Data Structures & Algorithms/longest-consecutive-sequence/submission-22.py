class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = 0
        if len(nums)>0:
            start= 1
        longest = start
        curr = start

        prev = -10000
        stuff = set()
        for num in nums:
            stuff.add(num)

        for num in sorted(nums):
            # If it's a duplicate
            if num == prev:
                continue
                
            # If it's consecutive
            elif num +1 in stuff:
                curr += 1
                
            # If there's a gap
            else:
                longest = max(longest, curr)
                curr = 1
            prev = num
        return longest

            
            

        