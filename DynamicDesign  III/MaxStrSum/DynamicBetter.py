def BettermaxSubSum(a):  # 加上记录器.
    dp = [0] * len(a)  # 构建一维DP数组[0*length]
    maxSum = dp[0] = a[0]  # 初始化dp首项&计数器
    startsit = endsit = 0
    for i in range(1, len(a)):  # i遍历项数
        dp[i] = max(dp[i - 1] + a[i], a[i])  # 核心: 当前序列要么取之前的缺一个当前项的序列加上当前指向元素, 要么重新开始取,看哪个更大.
        if dp[i] == a[i]:  # 发现重开了,则需要重新记录开始位置
            startsit = int(i)+1
        if dp[i] > maxSum:  # 如果发现取到了更大的,记得更新max
            maxSum = dp[i]
            endsit = int(i)+1

    return maxSum, startsit, endsit
