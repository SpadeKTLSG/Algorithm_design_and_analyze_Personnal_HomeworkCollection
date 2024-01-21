def BettermaxSubSum(a):  # ���ϼ�¼��.
    dp = [0] * len(a)  # ����һάDP����[0*length]
    maxSum = dp[0] = a[0]  # ��ʼ��dp����&������
    startsit = endsit = 0
    for i in range(1, len(a)):  # i��������
        dp[i] = max(dp[i - 1] + a[i], a[i])  # ����: ��ǰ����Ҫôȡ֮ǰ��ȱһ����ǰ������м��ϵ�ǰָ��Ԫ��, Ҫô���¿�ʼȡ,���ĸ�����.
        if dp[i] == a[i]:  # �����ؿ���,����Ҫ���¼�¼��ʼλ��
            startsit = int(i)+1
        if dp[i] > maxSum:  # �������ȡ���˸����,�ǵø���max
            maxSum = dp[i]
            endsit = int(i)+1

    return maxSum, startsit, endsit
