class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles) 
        total_time = -1
        def f(time): 
            total = 0
            for n in piles:
                total += ceil(n/time) 
            return total
        while start<= end: 
            mid = (start+end ) //2 
            if f(mid) <= h: 
                end = mid -1 
            else: 
                start = mid+1 
        return start