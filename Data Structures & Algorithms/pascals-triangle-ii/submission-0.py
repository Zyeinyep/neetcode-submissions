class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[] for _ in range(rowIndex + 1)]
        dp[0] = [1]
        for i in range(1,rowIndex+1):
            arr = []
            for j in range(i+1):
                a,b =0,0
                if j-1> -1:
                    a = dp[i-1][j-1]
                if j < i:
                    b = dp[i-1][j]
                arr.append(a+b)
            dp[i] = arr
        return dp[rowIndex]
        

        