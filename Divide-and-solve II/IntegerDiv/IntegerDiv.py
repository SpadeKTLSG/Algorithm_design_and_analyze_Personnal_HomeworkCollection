# -*- coding: gbk -*- 

"""���հ�.
Integer Division - divide by Python -


Question : ʵ�����������㷨��ͨ��ʵ����֤
�㷨˼·��
��������������ǽ�һ����������ֳ����ɸ��������ĺͣ�ʹ����Щ�������ĺ͵���ԭ������������
���磬����4���Բ�ֳ�1+1+1+1��1+1+2��1+3��2+2��4�������ֲ�ͬ�Ĳ�ַ�����


2��˼·: DP���� / �ݹ�(��ι���,����ը,���Ƽ�

ʹ�ö�̬�滮�㷨�����������⡣���ȶ���һ����ά����dp������dp[i][j]��ʾ��������i��ֳ����ɸ��������ĺͣ�����������Ϊj�ķ�������
��Ҫ�ر�ע����ǣ�������㷨ʱ�临�Ӷ�ΪO(n^2)����n�ϴ�ʱ����Ȼ���ܻ��������ʱ������������

�ݹ��㷨��ʱ�临�ӶȽϸߣ����п��ܻᵼ���ڼ���ϴ��������������ʱ����ջ��������⣬���ʺϼ���ϴ�������������⡣"""


def integer_partition(n):  # �����㷨: һά���ά
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # ���ﴴ����DP�������洢��������������㷨������.
    # DP[i][j]��ʾ��i����Ϊ���ɸ�����֮��(������,�²�׸��),������������������������j, �����ά�����ж����ֵΪ��Ӧ�ķ�����.

    for i in range(1, n + 1):  # ��ʼ��DP��������: ��ʵ������ͨ����ʶ�趨�������еĽ���,�������ѹ��
        dp[i][i] = 1  # �ܼ�: ��4����, ���������4���Ԫ��������, ��ô������ֻ��һ�ֻ��ַ���: 4�Լ�.
        dp[i][1] = 1  # ������: ��4����, �����������1��ֻ���ܶ���1,��ֻ��һ�ַ���.

    # ���Ĳ���:��DP����
    for i in range(3, n + 1):  # i��3ѭ����n,�ж�����Ԫ��.
        for j in range(2, i):  # j��2ѭ����i-1, ����ö������������j, �϶���2��ʼ,һֱ��i����
            if i - j >= j:  # �Ƚ���ɢ�ķַ�:����Ϊ��j��ɵ����ɸ��������ĺ�.
                dp[i][j] = dp[i - j][j] + dp[i - j][j - 1]
            else:  # �ȽϽ��յķַ�:����Ϊ��i-j�����������С��j����������֮��
                dp[i][j] = dp[i - j][i - j] + dp[i - j][j - 1] if (i - j != j - 1) | (j % 2 != 0) else dp[i - j][i - j]
    return sum(dp[n][:n + 1])  # dp[n][j]��ʾ��n����,���������������j�ķ���, ��Ϊ������n������������.


'''������������,�����⵽��һ������: Dp[5][2]Ԫ�ص�ֵ����Ϊ3,ʵ����ֻ��2( 221��21111���ֻ��� ). ���3�����·����DP[3][1]+DP[3][2]=1+2=3.
�����Ӧ��2��DPԪ����ӵĺ�����: {111}+({21}+{12})=3��, ��������DP[3][2]�ظ���.
��ôȥ���DP[3][2]����������, ����:  dp[i - j][i - j] �� dp[i - j][j - 1]���ظ���, �ʲ²������������.���ȥ����.

�������������DP[5][3] = 311 & 32 ������2,�������Ϊ1 ����: [2][2] + [2][2]������2 ,�����˲���,���ֻ��1. �������ǲ�������������
����,����������Ҫ����һ��j%2�����Ƶ�(��������)
���ͳ�������....Help!


������׼����ѧ��ǰ����, ������������һ��ҹ��ڶ�������������ͷ����: ����һֱ������ͺܿ������㷨д��������
����һ�����ƹ�ʽ����: 

��n=1��m=1ʱ��f(n,m)=1�� �ϻ�

��n<mʱ��f(n,m)=f(n,n)�� �ϻ�

��n=mʱ��f(n,m)=f(n,m-1)+1�� ������޸ĵ�����

��n>mʱ��f(n,m)=f(n,m-1)+f(n-m,m)��  ������޸ĵ�

����ֻ��һ��������������Ĳ��а�,�����һ��������������Ұ�.'''


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


# �����ۼ�ȫ�ֱ���
times = 0


# �����ݹ��㷨1

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


# �����ݹ��㷨2 :���ио���

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


# ����


# �ݹ�1
print(integer_par_recursion(6))
print(integer_par_recursion(5))
print(integer_par_recursion(4))
print(integer_par_recursion(3), "from�ݹ�ѡ��1")

# �ݹ�2
print(int_divide_recursion2(6, 6))
print(int_divide_recursion2(5, 5))
print(int_divide_recursion2(4, 4))
print(int_divide_recursion2(3, 3), "from�ݹ�ѡ��2")

# ����Dp
print(Great_partition(6, 6))
print(Great_partition(5, 5))
print(Great_partition(4, 4))
print(Great_partition(3, 3), "from����ѡ��")
