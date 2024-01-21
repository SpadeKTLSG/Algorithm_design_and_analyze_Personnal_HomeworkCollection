def maxCrossSum(a, left, mid, right):
    sumNUm2 = sumNUm1 = leftSum = rightSum = 0  # ��ʼ��������

    for i in range(mid, left - 1, -1):  # ��->�����Ѱ��ƴ��
        sumNUm1 += a[i]
        if sumNUm1 > leftSum:
            leftSum = sumNUm1

    for i in range(mid + 1, right + 1):  # ��->��Ѱ��Ѱ��ƴ��
        sumNUm2 += a[i]
        if sumNUm2 > rightSum:
            rightSum = sumNUm2

    return leftSum + rightSum  # ���Ϊ�������֮��


def maxS(a, left, right):
    if left == right:  # ��������һ����,�������Ҷ�ӦԪ�ظ����
        return a[left] if a[left] > 0 else 0
    mid = (left + right) // 2  # ����������
    leftSum = maxS(a, left, mid)  # dive into them
    rightSum = maxS(a, mid + 1, right)
    crossSum = maxCrossSum(a, left, mid, right)  # CrossPart
    return max(leftSum, rightSum, crossSum)  # ����������ȡ���


def maxSubSum(a):  # ���η�.
    return maxS(a, 0, len(a) - 1)  # ѡȡλ��:ͷ-β.
