def mat(s,p):
    r, c= (len(s), len(p))
    if r==0 and c==0:
        return True
    if c==0:
        return False
    dp =[[False for j in range(c+1)]for i in range(r+1)]
    dp[0][0]=True
    for i in range(2,c+1):
        if p[i-1]=='*':
            dp[0][i]=dp[0][i-2]
    for i in range(1,r+1):
        for j in range(1,c+1):
            if s[i-1]==p[j-1] or p[j-1]=='.':
                dp[i][j]=dp[i-1][j-1]
            elif j>1 and p[j-1]=='*':
                dp[i][j]=dp[i][j-2]
                if p[j-2]=='.'or p[j-2]==s[i-1]:
                    dp[i][j]= dp[i][j] or dp[i-1][j]
    return dp[r][c]
s=input("Enter  string :")
p=input("Enter pattern :")
print(mat(s,p))
