# -*- coding: gbk -*-
# 一个单位时间任务是恰好需要一个单位时间完成的任务。给定一个单位时间任务的有限集S。
# 关于S的一个时间表用于描述S中单位时间任务的执行次序。时间表中第1个任务从时间0 开始执行直至时间1 结束，
# 第2 个任务从时间1 开始执行至时间2 结束，…，第n个任务从时间n-1 开始执行直至时间n结束。


# 具有截止时间和误时惩罚的单位时间任务时间表问题可描述如下。
# (1) n个单位时间任务的集合S={1,2,…,n}；
# (2) 任务i的截止时间di ,1≤i≤n,1≤ di ≤n，即要求任务i在时间di 之前结束；
# (3) 任务i的误时惩罚wi ,1≤i≤n,即任务i未在时间di 之前结束将招致wi 的惩罚；若按时完成则无惩罚。

# 已知：给定的n 个单位时间任务，各任务的截止时间di ,各任务的误时惩罚wi ,1≤i≤n，
# 要求：确定S的一个时间表（最优时间表）使得总误时惩罚达到最小。
# 做得完有奖励,做不完有惩罚,求最小惩罚 :(

# 说明贪心选择


# 将所有的任务按照误时惩罚wi 从大到小排序，得到一个序列S。
# 初始化一个空的时间表solution。
# 对于S中的每个任务，按顺序选择下一个任务i，并检查是否可以在截止时间di 之前完成。如果可以，就将任务i 加入到solution中；如果不可以，就跳过任务i。
# 返回solution作为最优时间表。
import random


# 定义一个任务类，包含任务编号，截止时间和误时惩罚
class Task:
    def __init__(self, id, deadline, penalty):
        self.id = id
        self.deadline = deadline
        self.penalty = penalty

    # 定义一个比较函数，按照误时惩罚从大到小排序
    def __lt__(self, other):
        return self.penalty > other.penalty


# 定义一个函数，根据给定的任务集合，返回一个最优时间表
def schedule(tasks):
    tasks.sort()  # 将任务按照误时惩罚从大到小排序
    solution = []  # 初始化一个空的时间表
    slots = [False] * len(tasks)  # 初始化一个空的时间槽数组，用于记录每个时间槽是否被占用

    for task in tasks:  # 对于每个任务，按顺序选择下一个任务

        for i in range(task.deadline - 1, -1, -1):  # 从任务的截止时间开始向前寻找一个空闲的时间槽
            if not slots[i]:  # 贪心:如果找到了一个空闲的时间槽，就将任务放入该时间槽，并将其加入到时间表中
                slots[i] = True
                solution.append(task)
                break
    # 返回最优时间表
    return solution


# 定义一个函数，根据给定的参数，生成一组随机的任务
def generate_tasks(n, d_min, d_max, p_min, p_max):
    # 初始化一个空的任务集合
    tasks = []
    # 对于每个编号，生成一个随机的截止时间和误时惩罚，并创建一个任务对象
    for i in range(1, n + 1):
        deadline = random.randint(d_min, d_max)
        penalty = random.randint(p_min, p_max)
        task = Task(i, deadline, penalty)
        # 将任务对象加入到任务集合中
        tasks.append(task)
    # 返回任务集合
    return tasks


# 测试代码
# 指定任务的数量为10，截止时间的范围为1到10，误时惩罚的范围为10到100
n = 10
d_min = 1
d_max = 10
p_min = 10
p_max = 100
# 调用函数，生成一组随机的任务
tasks = generate_tasks(n, d_min, d_max, p_min, p_max)

# 打印生成的任务信息
print("The generated tasks are:")
for task in tasks:
    print("Task", task.id, "deadline:", task.deadline, "penalty:", task.penalty)

print("\n\n\n")
# 调用函数，得到最优时间表
solution = schedule(tasks)

# 打印结果
print("The optimal schedule is:")
for task in solution:
    print("Task", task.id, ' + ', end='')
