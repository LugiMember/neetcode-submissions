class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = {}
        window = {}
        smallest = ""

        for char in t:
            required[char] = required.get(char, 0) + 1

        if not t:
            return ""

        left = 0
        have = 0
        need = len(required)

        for right in range(len(s)):

            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in required and window[s[right]] == required[s[right]]:
                have += 1

            while have == need:
                current = s[left:right + 1]

                if smallest == "" or len(current) < len(smallest):
                    smallest = current

                window[s[left]] = window.get(s[left], 0) - 1

                if s[left] in required and window[s[left]] < required[s[left]]:
                    have -= 1

                left += 1

        return smallest