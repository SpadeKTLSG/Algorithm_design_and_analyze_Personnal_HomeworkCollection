# -*- coding: gbk -*- 
# Permutation - All in Order by Python -

# Question : 求n个元素的全排列，n个元素中允许出现重复元素，通过实例验证算法。

def permutation(something):  # 主方法.
    res = []
    used = [False] * len(something)  # 构建标记列表:元素长度个false
    something.sort()  # 先将传入的排序，方便去重
    backtrack(something, [], used, res)  # 开始调用回溯算法, 结果保存在res里, 新传入一个未命名path列表
    return res


# 递归-分治法设计策略:  1 结束器,  2 分治过程:把大问题化为子问题  3 进入子问题, 标记状态  4. 恢复现场, 标记还原

def backtrack(num, path, used, res):
    # ? 1 Terminator
    if len(path) == len(num):  # 如果当前path中元素的个数已经与总的元素个数相等,即都找到了, 就停止继续搜索.
        res.append(path[:])
        # ? 2 process result
        return  # 由于python的参数是引用类型, 因此不用管传值,只要直接返回最后取res即可.

    # 核心for循 : 在字符个数间do some iteration
    for i in range(len(num)):
        if not used[i]:  # 进入前提: 未取过该元素

            # ? 3 process current logic
            if i > 0 and num[i] == num[i - 1] and not used[i - 1]:  # 去重器:发现当前位置上的数和前一个位置上的数相同，并且前一个位置上的数还没被使用过，那么就可以跳过这个位置，避免重复。
                continue  # 这个去重器的设置是最大的难点, I think

            used[i] = True  # 来都来了, 先标记我来过了.
            path.append(num[i])  # 来都来了, 路径标记

            # ? 4 drill down
            backtrack(num, path, used, res)  # 进入子问题: 找下一个路径中的元素

            # ? 5 restore current status
            # 退出子问题就会来到这里, Bite the Dust !我回来了,恢复现场
            used[i] = False  # 继续尝试没取这个元素的情景
            path.pop()  # 同时记得把已经取这个元素的记录删除.


# 思路总结:
# 使用回溯算法五步法，从头到尾依次枚举每个位置上应该放置的数。
# 如果当前路径的长度已经等于数组的长度，就把这个路径加入到结果中,之后程序会自动尝试其他路径。
# 特别的,由于在本题中允许元素重复.因此我需要先将数组排序，方便给排在相邻元素之间进行去重。


# 测试
nums = [1, 2, 2]
killer = ['Killer Queen', 'King Crimson', 'White Snake']
helper = [114, 514, 1919, 810]
print(permutation(nums))  # 输出 [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
print(permutation(killer))
print(permutation(helper))
