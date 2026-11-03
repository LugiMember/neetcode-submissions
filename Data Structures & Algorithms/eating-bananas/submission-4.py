import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        high = piles[len(piles) - 1]
        low = 1
        smallest = high

        if len(piles) == h:
            return  high

        # try middle too slow? go up. Too fast? go down this is nlogn because u are searching through entire array log n times

        while low <= high:
            mid = (low + high)//2
            print("MID: ", mid)
            hours = 0
            for pile in piles:
                time = (pile + mid - 1) // mid #get ceiling
                hours += time

            print("HOURS", hours)
            print(hours< h)
            if hours > h:
                low = mid + 1
            else:
                if smallest > mid:
                    smallest = mid
                high = mid - 1
            print("LOW",low)
            print("HIGH", high)


        return smallest

        


        