class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,len(prices)
        buying,minimum=0,prices[0]
        profit=0
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-minimum)
            if prices[i]<minimum:
                buying=i
                minimum=prices[i]
        return profit

        