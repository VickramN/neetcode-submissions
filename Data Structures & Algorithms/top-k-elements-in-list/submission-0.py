class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for num in nums:
            sig = num

            if sig in groups:
                groups[sig] += 1
            else:
                groups[sig] = 1

        listFreq = [[] for _ in range(len(nums) + 1)]

        for sign in groups:
            frequency = groups[sign]
            listFreq[frequency].append(sign)

        result = []

        for i in range(len(listFreq) - 1, 0, -1):
            for num in listFreq[i]:
                result.append(num)

                if len(result) == k:
                    return result