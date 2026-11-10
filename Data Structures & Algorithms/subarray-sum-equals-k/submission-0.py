class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {}
        freq[0] = 1

        sum = 0
        output = 0
        for num in nums:
            sum += num
            diff = sum - k

            output += freq.get(diff, 0)

            freq[sum] = freq.get(sum, 0) + 1

        return output