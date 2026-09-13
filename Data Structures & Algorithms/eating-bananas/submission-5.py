class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            rate = (l + r) // 2

            # go through the pile to see if it is possible
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / rate)
            
            # check if we can go smaller
            if hours <= h:
                res = min(res, rate)
                r = rate - 1
            
            elif hours > h:
                l = rate + 1
        return res

