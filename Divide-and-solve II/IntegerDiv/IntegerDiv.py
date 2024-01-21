# -*- coding: gbk -*- 

"""最终版.
Integer Division - divide by Python -


Question : 实现整数划分算法，通过实例验证
算法思路：
整数划分问题就是将一个正整数拆分成若干个正整数的和，使得这些正整数的和等于原来的正整数。
例如，整数4可以拆分成1+1+1+1、1+1+2、1+3、2+2、4等若干种不同的拆分方法。


2种思路: DP数组 / 递归(层次过多,容易炸,不推荐

使用动态规划算法来解决这个问题。首先定义一个二维数组dp，其中dp[i][j]表示将正整数i拆分成若干个正整数的和，其中最大的数为j的方案数。
需要特别注意的是，本题的算法时间复杂度为O(n^2)，在n较大时，仍然可能会出现运算时间过长的情况。

递归算法的时间复杂度较高，极有可能会导致在计算较大的整数划分问题时出现栈溢出等问题，不适合计算较大的整数划分问题。"""


def integer_partition(n):  # 划分算法: 一维变二维
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # 这里创建了DP数组来存储计算的整数划分算法方案数.
    # DP[i][j]表示将i划分为若干个整数之和(正整数,下不赘述),并且其中最大的正整数不超过j, 这个二维数组中对象的值为对应的方案数.

    for i in range(1, n + 1):  # 初始化DP数组作用: 这实际上是通过常识设定程序运行的界限,减轻计算压力
        dp[i][i] = 1  # 很简单: 把4划分, 如果里面有4这个元素它本身, 那么它绝对只有一种划分方法: 4自己.
        dp[i][1] = 1  # 很容易: 把4划分, 里面最大数是1的只可能都是1,即只有一种方案.

    # 核心操作:对DP数组
    for i in range(3, n + 1):  # i从3循环到n,判断其余元素.
        for j in range(2, i):  # j从2循环到i-1, 用来枚举最大的正整数j, 肯定从2开始,一直到i以下
            if i - j >= j:  # 比较零散的分法:划分为由j组成的若干个正整数的和.
                dp[i][j] = dp[i - j][j] + dp[i - j][j - 1]
            else:  # 比较紧凑的分法:划分为由i-j和最大正整数小于j的若干整数之和
                dp[i][j] = dp[i - j][i - j] + dp[i - j][j - 1] if (i - j != j - 1) | (j % 2 != 0) else dp[i - j][i - j]
    return sum(dp[n][:n + 1])  # dp[n][j]表示将n划分,最大正整数不超过j的方案, 因为超不过n就这样可以了.


'''经过反复调试,这里检测到了一个问题: Dp[5][2]元素的值计算为3,实际上只有2( 221和21111两种划分 ). 获得3结果的路径是DP[3][1]+DP[3][2]=1+2=3.
问题对应的2个DP元素相加的含义是: {111}+({21}+{12})=3个, 很明显是DP[3][2]重复了.
那么去检查DP[3][2]的生命周期, 发现:  dp[i - j][i - j] 和 dp[i - j][j - 1]是重复的, 故猜测问题出在这里.添加去重器.

接下来问题出在DP[5][3] = 311 & 32 本该是2,这里计算为1 来自: [2][2] + [2][2]本该是2 ,触发了查重,结果只有1. 这下又是查重器的问题了
啊这,手算后好像是要加上一个j%2来控制的(胡言乱语)
最后就成了这样....Help!


本来是准备问学长前辈了, 经过反复碰壁一整夜后第二晨起来决定从头搞起: 查重一直出问题就很可能是算法写的有问题
换了一个递推公式如下: 

当n=1或m=1时，f(n,m)=1； 废话

当n<m时，f(n,m)=f(n,n)； 废话

当n=m时，f(n,m)=f(n,m-1)+1； 这个是修改的内容

当n>m时，f(n,m)=f(n,m-1)+f(n-m,m)。  这个是修改的

发现只有一个参数好像是真的不行啊,如果有一个参数的请告诉我吧.'''


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


# 次数累加全局变量
times = 0


# 暴力递归算法1

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


# 暴力递归算法2 :更有感觉了

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


# 测试


# 递归1
print(integer_par_recursion(6))
print(integer_par_recursion(5))
print(integer_par_recursion(4))
print(integer_par_recursion(3), "from递归选手1")

# 递归2
print(int_divide_recursion2(6, 6))
print(int_divide_recursion2(5, 5))
print(int_divide_recursion2(4, 4))
print(int_divide_recursion2(3, 3), "from递归选手2")

# 分治Dp
print(Great_partition(6, 6))
print(Great_partition(5, 5))
print(Great_partition(4, 4))
print(Great_partition(3, 3), "from分治选手")
