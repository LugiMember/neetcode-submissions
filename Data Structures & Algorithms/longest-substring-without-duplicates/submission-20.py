from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = deque()
        set_1 = set()
        longest = 0
        curr_longest = 0

        for char in s:
            if char not in set_1:
                seen.append(char)
                set_1.add(char)
                curr_longest += 1
            else:
                    # pop left until u get the char
                removed = 0
                while True:
                    removed += 1
                    temp = seen.popleft()
                    set_1.remove(temp)
                    if temp == char:
                        break

                seen.append(char)
                set_1.add(char)
                curr_longest = curr_longest - removed + 1
                     
            if curr_longest > longest:
                    longest = curr_longest


        return longest
        