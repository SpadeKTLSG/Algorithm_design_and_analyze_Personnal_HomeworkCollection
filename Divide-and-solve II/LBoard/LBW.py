# -*- coding: gbk -*- 
# LBoard_cover - LBC by Python -
# 
# "���Ѿ�����,������ǿ������!"
# ����������
# ��һ�� 2^k * 2^k ������ɵ������У���ǡ��һ����������������ͬ���Ƹ÷���Ϊ���ⷽ���ҳƸ�����Ϊ��������(Defective Chessboard)��
# �������̿��ǵ�k=2 ʱ16�����������е�һ���������̸��������У�Ҫ����ͼʾ��ʾ��4�ֲ�ͬ��״��L�͹��Ƹ��Ǹ��������ϳ����ⷽ����������з������κ�����L�͹��Ʒ��񲻵��ص������κ�һ��2k*2k �ĸ��������У��õ���L�͹��Ƹ���Ϊ(4^k-1)/3��
# ����˼·��ʹ�÷��η���˼·�����̸������⣬ͨ�������̵�����λ�÷���һ��L�ι��ƣ���ԭ�����ֳ��ĸ���ͬ��ģ�������⣬�ٶԸ���������ݹ���⡣
# �ݹ麯���ĳ���Ϊ��2*2�������з���һ��L�ι��ơ�

board_size = 8  # ��СΪ��׼�����������̴�С
tile = 0
label = 0

"""
board: ���̱������ָ��С�ĵ�Ԫ,�ö�ά�����ʾ,������һ��(���½�)���������
tr, tc: ���Ͻǵ���������
dr, dc: ���ⷽ�����������
size: ���̴�С
label: ���Ʊ��
"""


def cover(board, tr, tc, dr, dc, size):  # �ݹ���÷���,��������ʾ

    global tile
    global label
    if size == 1:
        return
    tile += 1
    sub_size = size 
    label += 1

        

    # ���ⷽ�������Ͻ�С������
    if dr < tr + sub_size and dc < tc + sub_size:
        cover(board, tr, tc, dr, dc, sub_size)
    else:
        # �������Ͻ�С�����ڣ��������Ͻ�С�������½�
        board[tr + sub_size - 1][tc + sub_size - 1] = label
        cover(board, tr, tc, tr + sub_size - 1, tc + sub_size - 1, sub_size)

    # ���ⷽ�������Ͻ�С������
    if dr < tr + sub_size and dc >= tc + sub_size:
        cover(board, tr, tc + sub_size, dr, dc, sub_size)
    else:
        # �������Ͻ�С�����ڣ��������Ͻ�С�������½�
        board[tr + sub_size - 1][tc + sub_size] = label
        cover(board, tr, tc + sub_size, tr + sub_size - 1, tc + sub_size, sub_size)

    # ���ⷽ�������½�С������
    if dr >= tr + sub_size and dc < tc + sub_size:
        cover(board, tr + sub_size, tc, dr, dc, sub_size)
    else:
        # �������½�С�����ڣ��������½�С�������Ͻ�
        board[tr + sub_size][tc + sub_size - 1] = label
        cover(board, tr + sub_size, tc, tr + sub_size, tc + sub_size - 1, sub_size)

    # ���ⷽ�������½�С������
    if dr >= tr + sub_size and dc >= tc + sub_size:
        cover(board, tr + sub_size, tc + sub_size, dr, dc, sub_size)
    else:
        # �������½�С�����ڣ��������½�С�������Ͻ�
        board[tr + sub_size][tc + sub_size] = label
        cover(board, tr + sub_size, tc + sub_size, tr + sub_size, tc + sub_size, sub_size)


# ���Դ���
# ��ʼ��
board1 = [['.' for _ in range(board_size)] for _ in range(board_size)]
board1[board_size - 1][board_size - 1] = '*'

# ��ӡ��ʼ״̬
for i in range(board_size):
    print(' '.join(board1[i]))

cover(board1, 0, 0, board_size - 1, board_size - 1, board_size)

print("\n�������\n")

for i in range(board_size):
    print(' '.join(str(board1[i])))

# ��������е�����...
print("\nL�͹�������:", tile)  # ==21


