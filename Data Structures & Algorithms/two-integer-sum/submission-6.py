class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                myList.append(i)
                myList.append(nums.index(temp, i + 1))
                break
                
        return myList