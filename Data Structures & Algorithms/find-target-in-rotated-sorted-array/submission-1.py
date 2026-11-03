class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #find how far the array was rotated

        # find roatation point and split the array in 2, do binary search on front and back half

        # to find rotation point we can use binary search
        left = 0
        right = len(nums) -1
        smallest = 0
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < nums[smallest]:
                smallest = mid
                
            if nums[mid] > nums[right]:
                left = mid + 1
            else: # if nums[mid] < nums[right] | num[mid] = nums[right]
                right = mid -1

        left = 0
        right = smallest -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid

        left = smallest
        right = len(nums) -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid


        return -1
            


        