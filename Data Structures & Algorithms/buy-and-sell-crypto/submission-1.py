class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minseen=prices[0]
        for i in prices[1:]:
            minseen=min(minseen,i)
            profit = max(profit,i-minseen)
        return profit

