class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiply all of them
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        
        output = []

        for num in nums:
            if zero_count == 0:
                output.append(product // num)
            elif zero_count == 1:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            elif zero_count >1:
                output.append(0)

        return output
