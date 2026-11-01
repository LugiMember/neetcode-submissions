class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = (right - left) * min(height[left], height[right])

        while left < right:
            left_wall = height[left]
            right_wall = height[right]

            # get width
            w = right - left

            # get height
            h = min(left_wall, right_wall)

            # get area
            area = w * h

            if max_area < area:
                max_area = area

            if left_wall < right_wall:
                left += 1
            else:
                right -= 1

        return max_area


