# -*- coding: gbk -*- 
# Strassen_matrix_multiply - SMM by Python -

import datetime  # ����ʱ��

"""Strassen����˷���һ�ֿ��پ���˷����㷨������ڴ�ͳ�ľ���˷��㷨������ʱ�临�Ӷȸ��ͣ��������ĳ������ӱȽϴ�������С��ģ����ļ����ϲ��紫ͳ���㷨��
Strassen����˷��ĺ���˼���ǽ�����������Բ�ֳ��ĸ��Ӿ��󣬲�ͨ��һЩ������������������ǵĳ˻���
M1 = (A11 + A22) �� (B11 + B22)
M2 = (A21 + A22) �� B11
M3 = A11 �� (B12 - B22)
M4 = A22 �� (B21 - B11)
M5 = (A11 + A12) �� B22
M6 = (A21 - A11) �� (B11 + B12)
M7 = (A12 - A22) �� (B21 + B22)


C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
������ĸ��Ӿ���C11��C12��C21��C22�������ָ�ϲ���һ��n��n�ľ���C���ɡ�"""


# Strassen����˷�pythonʾ��:
def strassen_matrix_multiply(A, B):
    u = len(A)
    if u == 1:
        return [[A[0][0] * B[0][0]]]

    # ������A��B�ֳ��ĸ��Ӿ���
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # �ݹ�����߸��˻�
    M1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # �����ĸ��Ӿ���C11��C12��C21��C22
    C11 = subtract_matrices(add_matrices(add_matrices(M1, M4), M7), M5)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = subtract_matrices(add_matrices(add_matrices(M1, M3), M6), M2)

    # �ϲ��ĸ��Ӿ���
    C = [[0 for j in range(u)] for i in range(u)]

    for i in range(u // 2):
        for j in range(u // 2):
            C[i][j] = C11[i][j]
            C[i][j + u // 2] = C12[i][j]
            C[i + u // 2][j] = C21[i][j]
            C[i + u // 2][j + u // 2] = C22[i][j]
    return C


def add_matrices(A, B):  # �������
    l = len(A)
    C = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract_matrices(A, B):  # �������
    m = len(A)
    C = [[0 for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):
            C[i][j] = A[i][j] - B[i][j]
    return C


def split_matrix(A):  # �����з�Ϊ4��
    k = len(A)
    m = k // 2
    A11 = [[0 for _ in range(m)] for _ in range(m)]
    A12 = [[0 for _ in range(m)] for _ in range(m)]
    A21 = [[0 for _ in range(m)] for _ in range(m)]
    A22 = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + m]
            A21[i][j] = A[i + m][j]
            A22[i][j] = A[i + m][j + m]
    return A11, A12, A21, A22


# ��ͳ����˷����԰������µĹ�ʽ�����㣺
# C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))

def matrix_multiply(A, B):
    o = len(A)
    C = [[0 for _ in range(o)] for _ in range(o)]
    for i in range(o):
        for j in range(o):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(o))
    return C


# ��ӡ����
def matrix_print(A):
    print('\n��ӡ����\n----------')
    for a in A:
        for row in a:
            print(row, end=' ')
        print()
    print('----------\n')


# ����

n = 4
matrix3 = [[5 for _ in range(n)] for _ in range(n)]
matrix32 = [[6 for _ in range(n)] for _ in range(n)]
n = 4
matrix4 = [[6 for _ in range(n)] for _ in range(n)]
matrix42 = [[7 for _ in range(n)] for _ in range(n)]
n = 4
matrix5 = [[7 for _ in range(n)] for _ in range(n)]
matrix52 = [[8 for _ in range(n)] for _ in range(n)]

#####
start1 = datetime.datetime.now()
matrix_out1 = strassen_matrix_multiply(matrix3, matrix32)
matrix_out2 = strassen_matrix_multiply(matrix4, matrix42)
matrix_out3 = strassen_matrix_multiply(matrix5, matrix52)
# ��ӡ���
matrix_print(matrix_out1)
matrix_print(matrix_out2)
matrix_print(matrix_out3)
end1 = datetime.datetime.now()

print('Strassen time is ', end1 - start1)
# Strassen time is  0.000999s

#####
start2 = datetime.datetime.now()
matrix_out1 = matrix_multiply(matrix3, matrix32)
matrix_out2 = matrix_multiply(matrix4, matrix42)
matrix_out3 = matrix_multiply(matrix5, matrix52)
# ��ӡ���
matrix_print(matrix_out1)
matrix_print(matrix_out2)
matrix_print(matrix_out3)
end2 = datetime.datetime.now()

print('Normal time is ', end2 - start2)
# Normal time is  0.001143s
