def maxSubSum(a):  # ������.
    maxSum = 0
    for i in range(len(a)):  # i: 0->len 
        for j in range(i, len(a)):  # j: i->len ѡȡ�Ķ���i֮�������
            thisSum = 0  # ��¼��ǰ��Sum
            for k in range(i, j + 1):  # k: i->j ��Ƭi��j֮����ֶ�
                thisSum += a[k]  # ���ϵ��ۼӶ�Ӧ��ֵ
            if thisSum > maxSum:  # ���ָ���,��update
                maxSum = thisSum
    return maxSum
