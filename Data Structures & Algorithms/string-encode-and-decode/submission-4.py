class Solution:

    def encode(self, strs: List[str]) -> str:
        flat = []
        for s in strs:
            flat.append(str(len(s)) + "_" + s) 
        return "".join(flat)

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0

        while i < len(s):
            underscore_idx = s.find("_", i)

            length = int(s[i:underscore_idx]) 
            
            start = underscore_idx + 1 # gets index of start
            end = start + length
            
            out.append(s[start:end])

            i = end
        return out

