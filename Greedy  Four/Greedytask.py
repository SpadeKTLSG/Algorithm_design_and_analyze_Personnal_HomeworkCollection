# -*- coding: gbk -*-
# һ����λʱ��������ǡ����Ҫһ����λʱ����ɵ����񡣸���һ����λʱ����������޼�S��
# ����S��һ��ʱ�����������S�е�λʱ�������ִ�д���ʱ����е�1�������ʱ��0 ��ʼִ��ֱ��ʱ��1 ������
# ��2 �������ʱ��1 ��ʼִ����ʱ��2 ������������n�������ʱ��n-1 ��ʼִ��ֱ��ʱ��n������


# ���н�ֹʱ�����ʱ�ͷ��ĵ�λʱ������ʱ���������������¡�
# (1) n����λʱ������ļ���S={1,2,��,n}��
# (2) ����i�Ľ�ֹʱ��di ,1��i��n,1�� di ��n����Ҫ������i��ʱ��di ֮ǰ������
# (3) ����i����ʱ�ͷ�wi ,1��i��n,������iδ��ʱ��di ֮ǰ����������wi �ĳͷ�������ʱ������޳ͷ���

# ��֪��������n ����λʱ�����񣬸�����Ľ�ֹʱ��di ,���������ʱ�ͷ�wi ,1��i��n��
# Ҫ��ȷ��S��һ��ʱ�������ʱ���ʹ������ʱ�ͷ��ﵽ��С��
# �������н���,�������гͷ�,����С�ͷ� :(

# ˵��̰��ѡ��


# �����е���������ʱ�ͷ�wi �Ӵ�С���򣬵õ�һ������S��
# ��ʼ��һ���յ�ʱ���solution��
# ����S�е�ÿ�����񣬰�˳��ѡ����һ������i��������Ƿ�����ڽ�ֹʱ��di ֮ǰ��ɡ�������ԣ��ͽ�����i ���뵽solution�У���������ԣ�����������i��
# ����solution��Ϊ����ʱ���
import random


# ����һ�������࣬���������ţ���ֹʱ�����ʱ�ͷ�
class Task:
    def __init__(self, id, deadline, penalty):
        self.id = id
        self.deadline = deadline
        self.penalty = penalty

    # ����һ���ȽϺ�����������ʱ�ͷ��Ӵ�С����
    def __lt__(self, other):
        return self.penalty > other.penalty


# ����һ�����������ݸ��������񼯺ϣ�����һ������ʱ���
def schedule(tasks):
    tasks.sort()  # ����������ʱ�ͷ��Ӵ�С����
    solution = []  # ��ʼ��һ���յ�ʱ���
    slots = [False] * len(tasks)  # ��ʼ��һ���յ�ʱ������飬���ڼ�¼ÿ��ʱ����Ƿ�ռ��

    for task in tasks:  # ����ÿ�����񣬰�˳��ѡ����һ������

        for i in range(task.deadline - 1, -1, -1):  # ������Ľ�ֹʱ�俪ʼ��ǰѰ��һ�����е�ʱ���
            if not slots[i]:  # ̰��:����ҵ���һ�����е�ʱ��ۣ��ͽ���������ʱ��ۣ���������뵽ʱ�����
                slots[i] = True
                solution.append(task)
                break
    # ��������ʱ���
    return solution


# ����һ�����������ݸ����Ĳ���������һ�����������
def generate_tasks(n, d_min, d_max, p_min, p_max):
    # ��ʼ��һ���յ����񼯺�
    tasks = []
    # ����ÿ����ţ�����һ������Ľ�ֹʱ�����ʱ�ͷ���������һ���������
    for i in range(1, n + 1):
        deadline = random.randint(d_min, d_max)
        penalty = random.randint(p_min, p_max)
        task = Task(i, deadline, penalty)
        # �����������뵽���񼯺���
        tasks.append(task)
    # �������񼯺�
    return tasks


# ���Դ���
# ָ�����������Ϊ10����ֹʱ��ķ�ΧΪ1��10����ʱ�ͷ��ķ�ΧΪ10��100
n = 10
d_min = 1
d_max = 10
p_min = 10
p_max = 100
# ���ú���������һ�����������
tasks = generate_tasks(n, d_min, d_max, p_min, p_max)

# ��ӡ���ɵ�������Ϣ
print("The generated tasks are:")
for task in tasks:
    print("Task", task.id, "deadline:", task.deadline, "penalty:", task.penalty)

print("\n\n\n")
# ���ú������õ�����ʱ���
solution = schedule(tasks)

# ��ӡ���
print("The optimal schedule is:")
for task in solution:
    print("Task", task.id, ' + ', end='')
