class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [0,1,0,0,0,1,0,0,0,0,0,0,0,0]
        """
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(1+dp[i-c],dp[i])
        return -1 if dp[-1]==amount+1 else dp[-1]

        
        