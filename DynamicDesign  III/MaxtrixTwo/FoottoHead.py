# !自底向上的动态规划方法
# 从最小的子问题开始，逐步扩大子问题的规模，直到求解原问题

# 输入的数据流构建:
# 假设p是一个列表，存储了n个矩阵的维度信息
# p[0]是第一个矩阵的行数，p[1]是第一个矩阵的列数（也是第二个矩阵的行数,依此类推
# n是矩阵的个数

# 定义一个二维数组m，用来存储 最优值 ，m[i][j]表示计算矩阵Ai…Aj的最少数乘次数。
# 定义一个二维数组s，用来存储 最优划分点 ，s[i][j]表示计算矩阵Ai…Aj时，最优的划分位置k。


def FH(p, n):  # 配置主函数,包含输出功能
    print(matrix_chain(p, n).index(1))  # 返回最优值
    s = matrix_chain(p, n).index(0)
    print_optimal(s, 0, len(s) - 1)  # 放输出里面去


def matrix_chain(p, n):
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]  # 创建两个n*n的二维数组m和s，初始化为0
    # 动态规划算法
    for k in range(2, n + 1):  # k表示子问题的规模
        for i in range(1, n - k + 2):  # i表示子问题的起始位置
            j = i + k - 1  # j表示子问题的终止位置
            m[i][j] = float('inf')  # 初始化最小代价为无穷大
            for k in range(i, j):  # k表示断开位置

                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]  # 计算当前断开位置的代价

                if q < m[i][j]:  # 如果当前代价小于之前的最小代价，更新最小代价和断开位置
                    m[i][j] = q
                    s[i][j] = k
    return m[1][n], s



def print_optimal(s, i, j):
    if i == j:
        print("A" + str(i), end="")  # 如果只有一个矩阵，则直接输出
    else:
        # 输出左括号
        print("(", end="")
        # 输出左边的子问题的最优解
        print_optimal(s, i, s[i][j])
        # 输出右边的子问题的最优解
        print_optimal(s, s[i][j] + 1, j)
        # 输出右括号
        print(")", end="")
