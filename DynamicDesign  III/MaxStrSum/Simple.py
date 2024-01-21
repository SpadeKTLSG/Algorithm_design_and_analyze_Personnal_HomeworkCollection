def maxSubSum(a):  # 暴力法.
    maxSum = 0
    for i in range(len(a)):  # i: 0->len 
        for j in range(i, len(a)):  # j: i->len 选取的对象i之后的区域
            thisSum = 0  # 记录当前的Sum
            for k in range(i, j + 1):  # k: i->j 切片i到j之间的字段
                thisSum += a[k]  # 不断地累加对应的值
            if thisSum > maxSum:  # 发现更大,则update
                maxSum = thisSum
    return maxSum
