class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        duplicateSet = set()

        for num in nums:
            if num in duplicateSet:
                return num
            else:
                duplicateSet.add(num)
        
        return 0