# -*-  coding:gbk -*-
# 最大子段和问题

from MaxStrSum.Simple import maxSubSum as SM1
from MaxStrSum.Divide import maxSubSum as SM2
from MaxStrSum.Dynamic import maxSubSum as SM3
from MaxStrSum.DynamicBetter import BettermaxSubSum as SM

a = [1, -2, 3, 5, -4, 6, 7, -3, 9]  # 结果为3加到9,23
b = [1, -7, 3, -3, 8, -4, 6, 7, -8, 9]  # 结果为8加到9,18
c = [6, -5, 3, -6, 5, -4, 7, 6, -7, -3, 5]  # 结果为5加到6,14

print("蛮力", SM1(a))
print("分治", SM2(a))
print("动态", SM3(a))
print('------------')
print("蛮力", SM1(b))
print("分治", SM2(b))
print("动态", SM3(b))
print('------------')
print("蛮力", SM1(c))
print("分治", SM2(c))
print("动态", SM3(c))

print('------打印序列位子(直观位子)------')
print("Better", SM(a))  # 3,9
print("Better", SM(b))  # 5,10
print("Better", SM(c))  # 5,8
