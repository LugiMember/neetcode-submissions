class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        max_left = [1] * len(height)
        max_right = [1] * len(height)


        # calc max_left
        curr_max = height[0]
        for i in range(len(height)):
            max_left[i] = curr_max
            if height[i] > curr_max:
                curr_max = height[i]


        # clac max_right
        curr_max = height[len(height) - 1]
        for i in range(len(height) -1, -1, -1):
            max_right[i] = curr_max
            if height[i] > curr_max:
                curr_max = height[i]

        output = 0

        for i in range(len(height)):
            curr = min(max_left[i], max_right[i]) - height[i]
            print(curr)
            if curr > 0:
                output += curr 

        return output

