# -*- coding: gbk -*- 

# 换了(借鉴了(超了(艺术不叫抄袭))一个递推公式如下: 
# 
# 当n=1或m=1时，f(n,m)=1； 废话
# 
# 当n<m时，f(n,m)=f(n,n)； 废话
# 
# 当n=m时，f(n,m)=f(n,m-1)+1； 这个是修改的内容
# 
# 当n>m时，f(n,m)=f(n,m-1)+f(n-m,m)。  这个是修改的

# 发现只有一个参数好像是真的不行啊,如果有一个参数的请告诉我吧.

def Great_partition(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]
    return dp[n][m]


print(Great_partition(6, 6))
print(Great_partition(5, 5))
print(Great_partition(4, 4))
print(Great_partition(3, 3), "分治选手:")
