# T:
# S:
# Leetcode:
# Issues: 


class Solution: 
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False]*(n+1) for _ in range(m+1)]                                # boolean dp matrix
        dp[0][0] = True                                                         

        for j in range(1,n+1):
            pChar = p[j-1]
            if pChar == "*":    
                dp[0][j] = dp[0][j-2]


        for i in range(1,m+1):
            for j in range(1,n+1):
                pChar = p[j-1]
                if pChar == "*":
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]

                else:
                    if pChar == s[i-1] or pChar == ".":
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        return dp[m][n]
