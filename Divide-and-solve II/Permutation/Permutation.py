# -*- coding: gbk -*- 
# Permutation - All in Order by Python -

# Question : ��n��Ԫ�ص�ȫ���У�n��Ԫ������������ظ�Ԫ�أ�ͨ��ʵ����֤�㷨��

def permutation(something):  # ������.
    res = []
    used = [False] * len(something)  # ��������б�:Ԫ�س��ȸ�false
    something.sort()  # �Ƚ���������򣬷���ȥ��
    backtrack(something, [], used, res)  # ��ʼ���û����㷨, ���������res��, �´���һ��δ����path�б�
    return res


# �ݹ�-���η���Ʋ���:  1 ������,  2 ���ι���:�Ѵ����⻯Ϊ������  3 ����������, ���״̬  4. �ָ��ֳ�, ��ǻ�ԭ

def backtrack(num, path, used, res):
    # ? 1 Terminator
    if len(path) == len(num):  # �����ǰpath��Ԫ�صĸ����Ѿ����ܵ�Ԫ�ظ������,�����ҵ���, ��ֹͣ��������.
        res.append(path[:])
        # ? 2 process result
        return  # ����python�Ĳ�������������, ��˲��ùܴ�ֵ,ֻҪֱ�ӷ������ȡres����.

    # ����forѭ : ���ַ�������do some iteration
    for i in range(len(num)):
        if not used[i]:  # ����ǰ��: δȡ����Ԫ��

            # ? 3 process current logic
            if i > 0 and num[i] == num[i - 1] and not used[i - 1]:  # ȥ����:���ֵ�ǰλ���ϵ�����ǰһ��λ���ϵ�����ͬ������ǰһ��λ���ϵ�����û��ʹ�ù�����ô�Ϳ����������λ�ã������ظ���
                continue  # ���ȥ�����������������ѵ�, I think

            used[i] = True  # ��������, �ȱ����������.
            path.append(num[i])  # ��������, ·�����

            # ? 4 drill down
            backtrack(num, path, used, res)  # ����������: ����һ��·���е�Ԫ��

            # ? 5 restore current status
            # �˳�������ͻ���������, Bite the Dust !�һ�����,�ָ��ֳ�
            used[i] = False  # ��������ûȡ���Ԫ�ص��龰
            path.pop()  # ͬʱ�ǵð��Ѿ�ȡ���Ԫ�صļ�¼ɾ��.


# ˼·�ܽ�:
# ʹ�û����㷨�岽������ͷ��β����ö��ÿ��λ����Ӧ�÷��õ�����
# �����ǰ·���ĳ����Ѿ���������ĳ��ȣ��Ͱ����·�����뵽�����,֮�������Զ���������·����
# �ر��,�����ڱ���������Ԫ���ظ�.�������Ҫ�Ƚ��������򣬷������������Ԫ��֮�����ȥ�ء�


# ����
nums = [1, 2, 2]
killer = ['Killer Queen', 'King Crimson', 'White Snake']
helper = [114, 514, 1919, 810]
print(permutation(nums))  # ��� [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
print(permutation(killer))
print(permutation(helper))
