def maxCrossSum(a, left, mid, right):
    sumNUm2 = sumNUm1 = leftSum = rightSum = 0  # 初始化计数器

    for i in range(mid, left - 1, -1):  # 中->左回退寻找拼接
        sumNUm1 += a[i]
        if sumNUm1 > leftSum:
            leftSum = sumNUm1

    for i in range(mid + 1, right + 1):  # 中->右寻找寻找拼接
        sumNUm2 += a[i]
        if sumNUm2 > rightSum:
            rightSum = sumNUm2

    return leftSum + rightSum  # 结合为左右最大之和


def maxS(a, left, right):
    if left == right:  # 左右碰在一起了,弹出左右对应元素更大的
        return a[left] if a[left] > 0 else 0
    mid = (left + right) // 2  # 划分子问题
    leftSum = maxS(a, left, mid)  # dive into them
    rightSum = maxS(a, mid + 1, right)
    crossSum = maxCrossSum(a, left, mid, right)  # CrossPart
    return max(leftSum, rightSum, crossSum)  # 左中右三者取最大


def maxSubSum(a):  # 分治法.
    return maxS(a, 0, len(a) - 1)  # 选取位置:头-尾.
