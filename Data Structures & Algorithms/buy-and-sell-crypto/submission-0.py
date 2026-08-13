class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minseen=1000000
        for i in prices:
            minseen=min(minseen,i)
            profit = max(profit,i-minseen)
        return profit

