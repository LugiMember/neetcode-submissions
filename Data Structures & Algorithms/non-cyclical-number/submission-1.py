class Solution:
    def isHappy(self, n: int) -> bool:
        #get digits

        #square and add digits

        #repeat this

        #while repeating this, check if the output has been seen before, if it hits 1 stop

        poop = set()
        curr = 0
        number = n

        while curr != 1:
            curr = 0
            for digit in str(number):
                curr += (int(digit) ** 2)
            number = curr
            if curr in poop:
                return False
            poop.add(curr)
        
        return True
            
