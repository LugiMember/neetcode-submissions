import heapq, math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for x, y in points:
            mag = math.pow(x, 2) + math.pow(y,2)
            heapq.heappush(heap, (mag, [x, y]))

        output = [0] * k
        for i in range(k):
            output[i] = heapq.heappop(heap)[1]

        return output