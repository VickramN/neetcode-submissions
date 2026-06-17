class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tString = "".join(sorted(t))
        sString = "".join(sorted(s))
        return tString == sString