class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        if len(nums) == 0:
            longest = 0
        else:
            longest = 1
        for num in nums:
            seen.add(num)

        for num in seen:
            streak = 1
            counter = num + 1
            if num - 1 in seen:
                continue
            while counter in seen:
                counter += 1
                streak += 1
            if longest < streak:
                 longest = streak

        return longest