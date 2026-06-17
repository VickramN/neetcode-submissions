class Solution:
    def isPalindrome(self, s: str) -> bool:
        sTemp = "".join(char for char in s if char.isalnum()).lower()
        sTempRev = sTemp[::-1]
        print(sTemp)
        print(sTempRev)
        return sTempRev == sTemp