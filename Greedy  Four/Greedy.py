# -*- coding: gbk -*-
# �㷨ʵ���,̰���㷨

# �������500��0/1�������⣨�����ģ������Խ�С�����ֱ�ʹ��̰���㷨�Ͷ�̬�滮�������

import random


# ̰��
def greedy_knapsack(weight, value, capacity):
    items = sorted(zip(weight, value), key=lambda x: x[1] / x[0], reverse=True)  # ����λ��ֵ������Ʒ, ʹ����lambda���ʽ���㵥λ��ֵ

    total_weight = 0  # ��ʼ�����
    total_value = 0

    for w, v in items:  # ������Ʒ

        if total_weight + w <= capacity:  # �����ǰ��Ʒ���Է��뱳��,�͸��ҷ���ݺݵ�̰��

            total_weight += w  # ���½��
            total_value += v
        else:
            continue  # ����������ǰ��Ʒ

    return total_value


# ��̬�滮�㷨
def dp_knapsack(weight, value, capacity):
    n = len(weight)  # ��ȡ��Ʒ����

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  # ��ʼ��״̬����

    for i in range(1, n + 1):  # ������Ʒ
        for j in range(1, capacity + 1):  # ������������
            # �����ǰ��Ʒ���Է��뱳��
            if weight[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])  # �ȽϷ���Ͳ�����ļ�ֵ��ȡ�ϴ���

            else:
                dp[i][j] = dp[i - 1][j]  # ����̳���һ��״̬

    return dp[n][capacity]  # ���ؽ��


def generate_test_data():  # ���ɲ������ݵĺ���

    n = random.randint(1, 10)  # ���������Ʒ�����ͱ�����������ΧΪ1��10
    capacity = random.randint(1, 10)

    # ���������Ʒ�����ͼ�ֵ����ΧΪ1��5
    weight = [random.randint(1, 5) for _ in range(n)]
    value = [random.randint(1, 5) for _ in range(n)]

    return n, capacity, weight, value  # ���ز�������


# Ӧ���㷨���: ��������

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


# ͳ��̰���㷨�������ֵ�ĸ���
# �����ֵ:̰��/��̬�滮:
# ͳ��Ӧ��̰���㷨���ʱ��ͳ��������������ж��:

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

print(f"�������ֵ�ĸ���: {count / n}")
print(f"��ֵ: {ratio / n}")
print(f"�����������: {max_error}")

