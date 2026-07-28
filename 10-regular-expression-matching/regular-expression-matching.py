class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match1 = {}
        def dp(i: int, j: int) -> bool:
            if (i, j) in match1:
                return match1[(i, j)]
            
            #Base Case
            if (j==len(p)):
                return i==len(s)

            #Check if current string matches
            first_match = i<len(s) and (p[j]==s[i] or p[j]=='.')

            #Handle * wildcard
            if j+1<len(p) and p[j+1]=='*':
                # Two choices: 
                # 1. Skip the '*' and its preceding element (zero occurrences)
                # 2. Consume one matching character from s and keep the '*'
                ans = dp(i, j + 2) or (first_match and dp(i+1, j))
            else:
                #No * continue normally
                ans = first_match and dp(i+1, j+1)
            
            match1[(i, j)] = ans
            return ans

        return dp(0,0)