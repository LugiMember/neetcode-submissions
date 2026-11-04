class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # lets say we keep a data structure maybe an stack of not found
        # we keep adding to it as we go through the array
        # we add the temperature and its index in a tuple

        stack = []
        result = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append((temp, i))

        return result