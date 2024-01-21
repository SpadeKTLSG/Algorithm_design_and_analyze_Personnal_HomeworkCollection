# -*- coding: gbk -*- 

# ����(�����(����(�������г�Ϯ))һ�����ƹ�ʽ����: 
# 
# ��n=1��m=1ʱ��f(n,m)=1�� �ϻ�
# 
# ��n<mʱ��f(n,m)=f(n,n)�� �ϻ�
# 
# ��n=mʱ��f(n,m)=f(n,m-1)+1�� ������޸ĵ�����
# 
# ��n>mʱ��f(n,m)=f(n,m-1)+f(n-m,m)��  ������޸ĵ�

# ����ֻ��һ��������������Ĳ��а�,�����һ��������������Ұ�.

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
print(Great_partition(3, 3), "����ѡ��:")
