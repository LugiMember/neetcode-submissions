class Solution:
     def firstUniqChar(self, s: str) -> int: 
        stuff = {} 

        for thing in s: 
            if thing in stuff:  
                stuff[thing] += 1
            else: 
                stuff[thing] = 1 

        for i in range(len(s)):
            if stuff[s[i]] == 1:
                return i

        return -1