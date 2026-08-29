class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum,price=0,prices[0]
        res=0
        for i in range(1,len(prices)):
            res=max(res,prices[i]-price)
            price=min(prices[i],price)
        return res
        