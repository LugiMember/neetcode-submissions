import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I would create frequency map
        freq = {}
        heap = []
        # go through each number in nums, adding one to the freq each time its seen
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:            
            curr = (freq[num], num)

            if len(heap) < k:
                heapq.heappush(heap, curr)
            else:
                if heap[0] < curr:
                    heapq.heappushpop(heap, curr)

        return [num for frequency, num in heap]
        # now for i unitl k, append to a list the top entries, and return this list
