class Solution:

    def encode(self, strs: List[str]) -> str:
            result = ""
            for s in strs:
                result += str(len(s)) + "&" + s
            
            return result
    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0

        while pointer < len(s):
            j = pointer
            while s[j] != "&":
                j += 1
            length = int(s[pointer:j])
            result.append(s[j+1: j+1+length])
            pointer = j + 1 + length

            
        return result
