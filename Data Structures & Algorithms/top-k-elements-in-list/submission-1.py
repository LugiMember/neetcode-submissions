class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I would create frequency map
        freq = {}

        # go through each number in nums, adding one to the freq each time its seen
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # create a list of the frequencies and sort it 
        out = sorted(freq, key=freq.get, reverse=True)

        return out[:k]        
        # now for i unitl k, append to a list the top entries, and return this list
