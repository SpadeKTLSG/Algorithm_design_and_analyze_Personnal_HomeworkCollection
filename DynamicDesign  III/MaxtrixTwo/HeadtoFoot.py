# !自顶向下的备忘录方法
# 从原问题开始，递归地求解子问题，并将已经求解过的子问题的结果存储起来，避免重复计算

# 输入的数据流构建:
# 假设p是一个列表，存储了n个矩阵的维度信息
# p[0]是第一个矩阵的行数，p[1]是第一个矩阵的列数（也是第二个矩阵的行数,依此类推
# n是矩阵的个数

# 定义一个二维数组m，用来存储最优值，m[i][j]表示计算矩阵Ai…Aj的最少数乘次数。
# 定义一个二维数组s，用来存储最优划分点，s[i][j]表示计算矩阵Ai…Aj时，最优的划分位置k。

# ----思路----
# 初始化m[i][j]为一个特殊值（如-1），表示该子问题还未求解过。
# 定义一个递归函数matrix_chain(i,j)，用来求解子问题m[i][j]和s[i][j]。
# 在函数中，如果m[i][j]不等于特殊值，说明该子问题已经求解过，直接返回m[i][j]。
# 否则，如果i等于j，说明单个矩阵不需要计算，将m[i][j]设为0，并返回0。
# 否则，遍历所有可能的划分位置k，比较不同划分方式的数乘次数，并记录最小值和对应的k。
# 将m[i][j]设为最小值，并返回该值。
# 调用matrix_chain(1,n)作为最优值，并根据s数组构造最优解。


def HF(p, n):  # 配置主函数,包含输出功能
    print(matrix_chain(p, n).index(1))  # 返回最优值
    s = matrix_chain(p, n).index(0)
    print_optimal(s, 0, len(s) - 1)


def matrix_chain(p, n):
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]  # 创建两个n*n的二维数组m和s，初始化为0
    matrix_chain_aux(p, m, s, 1, n)  # 调用递归函数来计算m[1][n]和s[1][n]
    return m[1][n], s  # 返回最优值和最优解


def matrix_chain_aux(p, m, s, i, j):  # 递归计算m[i][j]和s[i][j]

    # 两个边界条件(递归返回条件)
    if i == j:  # 如果i=j，那么m[i][j]=0，单个矩阵不需要计算
        m[i][j] = 0
        return m[i][j]

    if m[i][j] > 0:  # 另外如果m[i][j]不为0，说明已经计算过了，直接返回
        return m[i][j]

    m[i][j] = float('inf')  # 将m[i][j]设为infinity(无穷大)

    for k in range(i, j):  # 遍历所有可能的划分位置,k

        q1 = matrix_chain_aux(p, m, s, i, k)  # 计算左边的子问题的最优值

        q2 = matrix_chain_aux(p, m, s, k + 1, j)  # 计算右边的子问题的最优值

        q = q1 + q2 + p[i - 1] * p[k] * p[j]  # 计算当前划分的代价

        if q < m[i][j]:  # update m[i][j]和s[i][j]
            m[i][j] = q
            s[i][j] = k

    return m[i][j]


def print_optimal(s, i, j):  # 解释同前
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal(s, i, s[i][j])
        print_optimal(s, s[i][j] + 1, j)
        print(")", end="")
