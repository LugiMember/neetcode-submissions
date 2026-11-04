class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        if len(num) <= k:
            return "0"

        for digit_char in num:
            digit = int(digit_char)
            
            while stack and int(stack[-1]) > digit and k>0:
                stack.pop()
                k-=1

            stack.append(digit_char)

        while k > 0:
            stack.pop()
            k-=1

        output = "".join(stack).lstrip("0")

        return output if output else "0"

