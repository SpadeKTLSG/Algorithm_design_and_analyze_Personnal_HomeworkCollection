# -*-  coding:gbk -*-
# ����Ӷκ�����

from MaxStrSum.Simple import maxSubSum as SM1
from MaxStrSum.Divide import maxSubSum as SM2
from MaxStrSum.Dynamic import maxSubSum as SM3
from MaxStrSum.DynamicBetter import BettermaxSubSum as SM

a = [1, -2, 3, 5, -4, 6, 7, -3, 9]  # ���Ϊ3�ӵ�9,23
b = [1, -7, 3, -3, 8, -4, 6, 7, -8, 9]  # ���Ϊ8�ӵ�9,18
c = [6, -5, 3, -6, 5, -4, 7, 6, -7, -3, 5]  # ���Ϊ5�ӵ�6,14

print("����", SM1(a))
print("����", SM2(a))
print("��̬", SM3(a))
print('------------')
print("����", SM1(b))
print("����", SM2(b))
print("��̬", SM3(b))
print('------------')
print("����", SM1(c))
print("����", SM2(c))
print("��̬", SM3(c))

print('------��ӡ����λ��(ֱ��λ��)------')
print("Better", SM(a))  # 3,9
print("Better", SM(b))  # 5,10
print("Better", SM(c))  # 5,8
