# -*- coding: gbk -*- 
# Integer Division - divide by Python -


# Question : 实现整数划分算法，通过实例验证


# 思路: DP数组 / 递归(层次过多,容易炸,不推荐

def integer_partition(n):  # 划分算法: 一维变二维
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # 这里创建了DP数组来存储计算的整数划分算法方案数.
    # DP[i][j]表示将i划分为若干个整数之和(正整数,下不赘述),并且其中最大的正整数不超过j, 这个二维数组中对象的值为对应的方案数.

    for i in range(1, n + 1):  # 初始化DP数组作用: 这实际上是通过常识设定程序运行的界限,减轻计算压力
        dp[i][i] = 1  # 很简单: 把4划分, 如果里面有4这个元素它本身, 那么它绝对只有一种划分方法: 4自己.
        dp[i][1] = 1  # 很容易: 把4划分, 里面最大数是1的只可能都是1,即只有一种方案.

    # 核心操作:对DP数组
    for i in range(3, n + 1):  # i从3循环
        # 到n,判断其余元素.
        for j in range(2, i):  # j从2循环到i-1, 用来枚举最大的正整数j, 肯定从2开始,一直到i以下
            if i - j >= j:  # 划分为由j组成的若干个正整数的和.
                dp[i][j] = dp[i - j][j] + dp[i - j][j - 1]
            else:  # 划分为由i-j和最大正整数小于j的若干整数之和
                dp[i][j] = dp[i - j][i - j] + dp[i - j][j - 1]
    return sum(dp[n][:])  # dp[n][j]表示将n划分,最大正整数不超过j的方案, 因为超不过n就这样可以了.


# 经过反复调试,这里检测到了一个问题: Dp[5][2]元素的值计算为3,实际上只有2( 221和21111两种划分 ). 获得3结果的路径是DP[3][1]+DP[3][2]=1+2=3.
# 问题对应的2个DP元素相加的含义是: {111}+{21}+{12}=3个, 很明显是DP[3][2]重复了.
# 那么去检查DP[3][2]的生命周期, 发现:

# 次数累加变量
times = 0


def integer_par_recursion(n):
    global times
    times = 0
    int_divide(n, 1, {0: 0})  # 用python字典这个数据结构存储划分因子，从1开始，用0占位
    return times


def int_divide(number, index, dividing_number):
    # 从1开始遍历该整数所有划分因子
    global times
    for i in range(1, number + 1):

        if i >= dividing_number[index - 1]:  # 与前一位划分因子比较，去重，如先有24,42则不行
            dividing_number[index] = i  # 当前数-划分因子后还剩数，如6-1剩5

            number_rest = number - i  # 整数被划分完毕

            if number_rest == 0:
                # !这里可以选择输出划分因子
                # for j in range(1, index):
                #     print(str(dividing_number[j]) + '+', end='')
                # print(str(dividing_number[index]))
                times = times + 1

            else:  # 未被划分完毕，继续，dividing_Number划分位数+1
                int_divide(number_rest, index + 1, dividing_number)
        else:
            pass


def int_divide_recursion2(n, m):
    if n < 1 or m < 1:
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        return int_divide_recursion2(n, n)
    if n == m:
        return int_divide_recursion2(n, m - 1) + 1
    return int_divide_recursion2(n, m - 1) + int_divide_recursion2(n - m, m)


# 该代码是实现了整数划分问题的递归算法，其中n表示待划分的正整数，m表示可以使用的最大正整数。该算法的思路是：将n拆分成最大数为m的若干个正整数之和，不考虑顺序，返回方案数。
# 该递归算法的时间复杂度较高，可能会导致在计算较大的整数划分问题时出现栈溢出等问题，不适合计算较大的整数划分问题。

# 测试


# 递归1
print(integer_par_recursion(6))
print(integer_par_recursion(7))
print(integer_par_recursion(8))
print(integer_par_recursion(5))
print(integer_par_recursion(4))
print(integer_par_recursion(3), "from递归选手1")

# 递归2
print(int_divide_recursion2(6, 6))
print(int_divide_recursion2(5, 5))
print(int_divide_recursion2(4, 4))
print(int_divide_recursion2(3, 3), "from递归选手2")

# 分治Dp
print()
print(integer_partition(6))
print(integer_partition(5))
print(integer_partition(4))
print(integer_partition(3), "分治选手:")

#正确答案:
# 11
# 7
# 5
# 3

# 算法思路：
# 整数划分问题就是将一个正整数拆分成若干个正整数的和，使得这些正整数的和等于原来的正整数。例如，整数4可以拆分成1+1+1+1、1+1+2、1+3、2+2、4等若干种不同的拆分方法。在这个问题中，我们只需要算出正整数n共有多少种不同的拆分方法即可。
# 我们可以使用动态规划算法来解决这个问题。首先定义一个二维数组dp，其中dp[i][j]表示将正整数i拆分成若干个正整数的和，其中最大的数为j的方案数。显然，当j为1时，dp[i][j]的值为1，因为只有将i拆分成1+1+1+1+...+1这种方案。当i等于j时，dp[i][j]的值也为1，因为只有将i拆分成i这一种方案。对于其他情况，dp[i][j]可以分为两种情况讨论：一种是i-j>=j，这时将i拆分成若干个最大数为j的数和一个最大数为j的数；另一种是i-j<j，这时将i拆分成若干个最大数为i-j的数和一个最大数为j的数。这两种情况下的方案数分别为dp[i-j][j]+dp[i-1][j-1]和dp[i-j][i-j]+dp[i-1][j-1]。最后，将dp[n][1]到dp[n][n-1]的值相加，即为正整数n的所有拆分方案数。
# 需要特别注意的是，本题的算法时间复杂度为O(n^2)，因此在n较大时，可能会出现运算时间过长的情况。


# 代码实现的是整数划分问题，即将一个正整数N分成若干个正整数的和，不考虑顺序。
# 为了验证代码是否正确无误，我们需要先了解一下整数划分的概念和性质。整数划分问题是数学中的经典问题之一，其数学定义如下：
# 将正整数n拆分成若干个正整数之和的方案数，不考虑顺序。例如，对于n=5，可以拆分成以下7个不同的方案：
# 
# 
# 5
# 
# 4+1
# 
# 3+2
# 
# 3+1+1
# 
# 2+2+1
# 
# 2+1+1+1
# 
# 1+1+1+1+1
