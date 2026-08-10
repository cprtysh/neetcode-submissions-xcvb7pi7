class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, l, r = max(piles), 1, max(piles)
        while l <= r:
            m, hours = (l + r) // 2, 0
            for p in piles:
                hours -= (p // -m)
            if hours <= h:
                min_speed = min(m, min_speed)
                r = m - 1
            else:
                l = m + 1
        return min_speed