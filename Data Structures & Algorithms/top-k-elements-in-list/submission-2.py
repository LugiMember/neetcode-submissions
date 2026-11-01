class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I would create frequency map
        freq = {}
        heap = []
        # go through each number in nums, adding one to the freq each time its seen
        for num in nums:
            # maintain a min heap of k, replacing when min is suprassed

            freq[num] = freq.get(num, 0) + 1

        out = sorted(freq, key=freq.get, reverse=True)

        return out[:k]        
        # now for i unitl k, append to a list the top entries, and return this list
