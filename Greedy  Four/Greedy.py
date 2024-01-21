# -*- coding: gbk -*-
# 算法实验课,贪心算法

# 随机生成500个0/1背包问题（问题规模可以相对较小），分别使用贪心算法和动态规划进行求解

import random


# 贪心
def greedy_knapsack(weight, value, capacity):
    items = sorted(zip(weight, value), key=lambda x: x[1] / x[0], reverse=True)  # 按单位价值排序物品, 使用了lambda表达式计算单位价值

    total_weight = 0  # 初始化结果
    total_value = 0

    for w, v in items:  # 遍历物品

        if total_weight + w <= capacity:  # 如果当前物品可以放入背包,就给我放入狠狠的贪心

            total_weight += w  # 更新结果
            total_value += v
        else:
            continue  # 否则跳过当前物品

    return total_value


# 动态规划算法
def dp_knapsack(weight, value, capacity):
    n = len(weight)  # 获取物品数量

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # 初始化状态数组

    for i in range(1, n + 1):  # 遍历物品
        for j in range(1, capacity + 1):  # 遍历背包容量
            # 如果当前物品可以放入背包
            if weight[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])  # 比较放入和不放入的价值，取较大者

            else:
                dp[i][j] = dp[i - 1][j]  # 否则继承上一个状态

    return dp[n][capacity]  # 返回结果


def generate_test_data():  # 生成测试数据的函数

    n = random.randint(1, 10)  # 随机生成物品数量和背包容量，范围为1到10
    capacity = random.randint(1, 10)

    # 随机生成物品重量和价值，范围为1到5
    weight = [random.randint(1, 5) for _ in range(n)]
    value = [random.randint(1, 5) for _ in range(n)]

    return n, capacity, weight, value  # 返回测试数据


# 应用算法求解: 测试数据

# for u in range(5):
#     n, capacity, weight, value = generate_test_data()
#     print(f"Example {u + 1}:")
#     print(f"n = {n}")
#     print(f"capacity = {capacity}")
#     print(f"weight = {weight}")
#     print(f"value = {value}")
#     print(f"Greedy: {greedy_knapsack(weight, value, capacity)}")
#     print(f"DP: {dp_knapsack(weight, value, capacity)}")
#     print()


# 统计贪心算法求得最优值的概率
# 计算比值:贪心/动态规划:
# 统计应用贪心算法求解时，统计最坏的情况下误差有多大:

n = 1000
count = ratio = max_error = 0
for i in range(n):
    n, capacity, weight, value = generate_test_data()

    if (dp_knapsack(weight, value, capacity) == 0):
        continue
    else:
        if greedy_knapsack(weight, value, capacity) == dp_knapsack(weight, value, capacity):
            count += 1
        ratio += greedy_knapsack(weight, value, capacity) / dp_knapsack(weight, value, capacity)
        max_error = max(max_error, greedy_knapsack(weight, value, capacity) / dp_knapsack(weight, value, capacity))

print(f"求得最优值的概率: {count / n}")
print(f"比值: {ratio / n}")
print(f"最坏的情况下误差: {max_error}")

