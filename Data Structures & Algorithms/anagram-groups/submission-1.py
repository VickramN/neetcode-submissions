class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for string in strs:
            sig =[0]*26

            for c in string:
                sig[ord(c)-97] += 1
            sign = tuple(sig)
            if sign in groups:
                groups[sign].append(string)
            else:
                groups[sign] = [string]
        
        return list(groups.values())
            