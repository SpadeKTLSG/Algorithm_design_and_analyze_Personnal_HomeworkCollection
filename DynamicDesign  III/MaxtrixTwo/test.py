# -*-  coding:gbk -*-
from FoottoHead import matrix_chain as FH
from HeadtoFoot import matrix_chain as HF

# ������������
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
# һ����˵���Ե����ϵķ������Ӽ��͸�Ч����Ϊ�������˵ݹ���ô����Ŀ�����
# �Զ����µķ��������������Ȼ����Ϊ�����Ը�����Ҫ��������⡣
