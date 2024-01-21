def maxSubSum(a):  # ��̬�滮
    dp = [0] * len(a)  # ����һάDP����[0*length]
    maxSum = dp[0] = a[0]  # ��ʼ��dp����&������
    for i in range(1, len(a)):  # i��������,O(n)���Ӷ�.
        dp[i] = max(dp[i - 1] + a[i], a[i])  # ����: ��ǰ����Ҫôȡ֮ǰ��ȱһ����ǰ������м��ϵ�ǰָ��Ԫ��, Ҫô���¿�ʼȡ,���ĸ�����.
        if dp[i] > maxSum:  # �������ȡ���˸����,�ǵø���max
            maxSum = dp[i]
    return maxSum
