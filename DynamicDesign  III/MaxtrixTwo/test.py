# -*-  coding:gbk -*-
from FoottoHead import matrix_chain as FH
from HeadtoFoot import matrix_chain as HF

# 矩阵连乘问题
# test 3
p = [5, 10, 3, 12, 5, 50, 6]
n = len(p) - 1
FH(p, n)
HF(p, n)


p = [10, 20, 30, 40, 30]
n = len(p) - 1
FH(p, n)
HF(p, n)

p = [2, 3, 4, 5, 6]
n = len(p) - 1
FH(p, n)
HF(p, n)
# 一般来说，自底向上的方法更加简洁和高效，因为它避免了递归调用带来的开销。
# 自顶向下的方法则更加灵活和自然，因为它可以根据需要求解子问题。
