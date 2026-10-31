from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = deque()
        longest = 0
        curr_longest = 0

        for char in s:
            if char not in seen:
                seen.append(char)
                curr_longest += 1
            else:
                    # pop left until u get the char
                removed = 0
                while True:
                    removed += 1
                    if seen.popleft() == char:
                        break

                seen.append(char)
                curr_longest = curr_longest - removed + 1
                     
            if curr_longest > longest:
                    longest = curr_longest


        return longest
        