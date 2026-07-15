class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        poop = {}
        repeat = -1000

        sum = 0
        expected_sum = 0
        for row in grid:
            for num in row:
                poop[num] = poop.get(num, 0) + 1
                if poop[num] > 1:
                    repeat = num
                else:
                    sum += num

        for num in range(1, len(grid) ** 2 + 1):
            expected_sum += num

        diff = expected_sum - sum
        return [repeat, diff]
