import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = Counter(s)
        heap = [(-count, char) for char, count in freq.items()]


        heapq.heapify(heap)
        
        output = ""

        count, letter = heapq.heappop(heap)
        count += 1
        output += letter

        last = (count, letter)

        while heap:
            count, letter = heapq.heappop(heap)
            count += 1
            output += letter

            if last[0] < 0:
                heapq.heappush(heap, last)

            last = (count, letter)

        if(last[0] != 0):
            return ""
        return output
