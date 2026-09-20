class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingSpeed = max(piles)
        minEatingSpeed = 1
        res = maxEatingSpeed
        while minEatingSpeed <= maxEatingSpeed:

            k = (minEatingSpeed + maxEatingSpeed)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res,k)
                maxEatingSpeed = k -1
            else:
                minEatingSpeed = k + 1
        
        return res