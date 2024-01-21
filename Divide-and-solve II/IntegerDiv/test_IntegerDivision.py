# -*- coding: gbk -*- 
# Integer Division - divide by Python -


# Question : ʵ�����������㷨��ͨ��ʵ����֤


# ˼·: DP���� / �ݹ�(��ι���,����ը,���Ƽ�

def integer_partition(n):  # �����㷨: һά���ά
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # ���ﴴ����DP�������洢��������������㷨������.
    # DP[i][j]��ʾ��i����Ϊ���ɸ�����֮��(������,�²�׸��),������������������������j, �����ά�����ж����ֵΪ��Ӧ�ķ�����.

    for i in range(1, n + 1):  # ��ʼ��DP��������: ��ʵ������ͨ����ʶ�趨�������еĽ���,�������ѹ��
        dp[i][i] = 1  # �ܼ�: ��4����, ���������4���Ԫ��������, ��ô������ֻ��һ�ֻ��ַ���: 4�Լ�.
        dp[i][1] = 1  # ������: ��4����, �����������1��ֻ���ܶ���1,��ֻ��һ�ַ���.

    # ���Ĳ���:��DP����
    for i in range(3, n + 1):  # i��3ѭ��
        # ��n,�ж�����Ԫ��.
        for j in range(2, i):  # j��2ѭ����i-1, ����ö������������j, �϶���2��ʼ,һֱ��i����
            if i - j >= j:  # ����Ϊ��j��ɵ����ɸ��������ĺ�.
                dp[i][j] = dp[i - j][j] + dp[i - j][j - 1]
            else:  # ����Ϊ��i-j�����������С��j����������֮��
                dp[i][j] = dp[i - j][i - j] + dp[i - j][j - 1]
    return sum(dp[n][:])  # dp[n][j]��ʾ��n����,���������������j�ķ���, ��Ϊ������n������������.


# ������������,�����⵽��һ������: Dp[5][2]Ԫ�ص�ֵ����Ϊ3,ʵ����ֻ��2( 221��21111���ֻ��� ). ���3�����·����DP[3][1]+DP[3][2]=1+2=3.
# �����Ӧ��2��DPԪ����ӵĺ�����: {111}+{21}+{12}=3��, ��������DP[3][2]�ظ���.
# ��ôȥ���DP[3][2]����������, ����:

# �����ۼӱ���
times = 0


def integer_par_recursion(n):
    global times
    times = 0
    int_divide(n, 1, {0: 0})  # ��python�ֵ�������ݽṹ�洢�������ӣ���1��ʼ����0ռλ
    return times


def int_divide(number, index, dividing_number):
    # ��1��ʼ�������������л�������
    global times
    for i in range(1, number + 1):

        if i >= dividing_number[index - 1]:  # ��ǰһλ�������ӱȽϣ�ȥ�أ�������24,42����
            dividing_number[index] = i  # ��ǰ��-�������Ӻ�ʣ������6-1ʣ5

            number_rest = number - i  # �������������

            if number_rest == 0:
                # !�������ѡ�������������
                # for j in range(1, index):
                #     print(str(dividing_number[j]) + '+', end='')
                # print(str(dividing_number[index]))
                times = times + 1

            else:  # δ��������ϣ�������dividing_Number����λ��+1
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


# �ô�����ʵ����������������ĵݹ��㷨������n��ʾ�����ֵ���������m��ʾ����ʹ�õ���������������㷨��˼·�ǣ���n��ֳ������Ϊm�����ɸ�������֮�ͣ�������˳�򣬷��ط�������
# �õݹ��㷨��ʱ�临�ӶȽϸߣ����ܻᵼ���ڼ���ϴ��������������ʱ����ջ��������⣬���ʺϼ���ϴ�������������⡣

# ����


# �ݹ�1
print(integer_par_recursion(6))
print(integer_par_recursion(7))
print(integer_par_recursion(8))
print(integer_par_recursion(5))
print(integer_par_recursion(4))
print(integer_par_recursion(3), "from�ݹ�ѡ��1")

# �ݹ�2
print(int_divide_recursion2(6, 6))
print(int_divide_recursion2(5, 5))
print(int_divide_recursion2(4, 4))
print(int_divide_recursion2(3, 3), "from�ݹ�ѡ��2")

# ����Dp
print()
print(integer_partition(6))
print(integer_partition(5))
print(integer_partition(4))
print(integer_partition(3), "����ѡ��:")

#��ȷ��:
# 11
# 7
# 5
# 3

# �㷨˼·��
# ��������������ǽ�һ����������ֳ����ɸ��������ĺͣ�ʹ����Щ�������ĺ͵���ԭ���������������磬����4���Բ�ֳ�1+1+1+1��1+1+2��1+3��2+2��4�������ֲ�ͬ�Ĳ�ַ���������������У�����ֻ��Ҫ���������n���ж����ֲ�ͬ�Ĳ�ַ������ɡ�
# ���ǿ���ʹ�ö�̬�滮�㷨�����������⡣���ȶ���һ����ά����dp������dp[i][j]��ʾ��������i��ֳ����ɸ��������ĺͣ�����������Ϊj�ķ���������Ȼ����jΪ1ʱ��dp[i][j]��ֵΪ1����Ϊֻ�н�i��ֳ�1+1+1+1+...+1���ַ�������i����jʱ��dp[i][j]��ֵҲΪ1����Ϊֻ�н�i��ֳ�i��һ�ַ������������������dp[i][j]���Է�Ϊ����������ۣ�һ����i-j>=j����ʱ��i��ֳ����ɸ������Ϊj������һ�������Ϊj��������һ����i-j<j����ʱ��i��ֳ����ɸ������Ϊi-j������һ�������Ϊj����������������µķ������ֱ�Ϊdp[i-j][j]+dp[i-1][j-1]��dp[i-j][i-j]+dp[i-1][j-1]����󣬽�dp[n][1]��dp[n][n-1]��ֵ��ӣ���Ϊ������n�����в�ַ�������
# ��Ҫ�ر�ע����ǣ�������㷨ʱ�临�Ӷ�ΪO(n^2)�������n�ϴ�ʱ�����ܻ��������ʱ������������


# ����ʵ�ֵ��������������⣬����һ��������N�ֳ����ɸ��������ĺͣ�������˳��
# Ϊ����֤�����Ƿ���ȷ����������Ҫ���˽�һ���������ֵĸ�������ʡ�����������������ѧ�еľ�������֮һ������ѧ�������£�
# ��������n��ֳ����ɸ�������֮�͵ķ�������������˳�����磬����n=5�����Բ�ֳ�����7����ͬ�ķ�����
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