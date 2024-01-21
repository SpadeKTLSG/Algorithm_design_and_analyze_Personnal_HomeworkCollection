# -*- coding: gbk -*- 
# LBoard_cover - LBC by Python -
# 
# "我已经拿起,最初的那块骨牌了!"
# 问题描述：
# 在一个 2^k * 2^k 方格组成的棋盘中，若恰有一个方格与其他方格不同，称该方格为特殊方格，且称该棋盘为特殊棋盘(Defective Chessboard)。
# 特殊棋盘块是当k=2 时16个特殊棋盘中的一个，在棋盘覆盖问题中，要求用图示所示的4种不同形状的L型骨牌覆盖给定棋盘上除特殊方格以外的所有方格，且任何俩个L型骨牌方格不得重叠。在任何一个2k*2k 的覆盖棋盘中，用到的L型骨牌个数为(4^k-1)/3。
# 解题思路：使用分治法的思路，棋盘覆盖问题，通过在棋盘的中心位置放置一个L形骨牌，将原问题拆分成四个相同规模的子问题，再对各个子问题递归求解。
# 递归函数的出口为在2*2的棋盘中放置一个L形骨牌。

board_size = 8  # 大小为标准国际象棋棋盘大小
tile = 0
label = 0

"""
board: 棋盘本身或是指更小的单元,用二维数组表示,其中有一个(右下角)定义的死点
tr, tc: 左上角的行列坐标
dr, dc: 特殊方块的行列坐标
size: 棋盘大小
label: 骨牌标记
"""


def cover(board, tr, tc, dr, dc, size):  # 递归调用方法,参数如所示

    global tile
    global label
    if size == 1:
        return
    tile += 1
    sub_size = size 
    label += 1

        

    # 特殊方块在左上角小棋盘内
    if dr < tr + sub_size and dc < tc + sub_size:
        cover(board, tr, tc, dr, dc, sub_size)
    else:
        # 不在左上角小棋盘内，覆盖左上角小棋盘右下角
        board[tr + sub_size - 1][tc + sub_size - 1] = label
        cover(board, tr, tc, tr + sub_size - 1, tc + sub_size - 1, sub_size)

    # 特殊方块在右上角小棋盘内
    if dr < tr + sub_size and dc >= tc + sub_size:
        cover(board, tr, tc + sub_size, dr, dc, sub_size)
    else:
        # 不在右上角小棋盘内，覆盖右上角小棋盘左下角
        board[tr + sub_size - 1][tc + sub_size] = label
        cover(board, tr, tc + sub_size, tr + sub_size - 1, tc + sub_size, sub_size)

    # 特殊方块在左下角小棋盘内
    if dr >= tr + sub_size and dc < tc + sub_size:
        cover(board, tr + sub_size, tc, dr, dc, sub_size)
    else:
        # 不在左下角小棋盘内，覆盖左下角小棋盘右上角
        board[tr + sub_size][tc + sub_size - 1] = label
        cover(board, tr + sub_size, tc, tr + sub_size, tc + sub_size - 1, sub_size)

    # 特殊方块在右下角小棋盘内
    if dr >= tr + sub_size and dc >= tc + sub_size:
        cover(board, tr + sub_size, tc + sub_size, dr, dc, sub_size)
    else:
        # 不在右下角小棋盘内，覆盖右下角小棋盘左上角
        board[tr + sub_size][tc + sub_size] = label
        cover(board, tr + sub_size, tc + sub_size, tr + sub_size, tc + sub_size, sub_size)


# 测试代码
# 初始化
board1 = [['.' for _ in range(board_size)] for _ in range(board_size)]
board1[board_size - 1][board_size - 1] = '*'

# 打印开始状态
for i in range(board_size):
    print(' '.join(board1[i]))

cover(board1, 0, 0, board_size - 1, board_size - 1, board_size)

print("\n处理完毕\n")

for i in range(board_size):
    print(' '.join(str(board1[i])))

# 输出可能有点问题...
print("\nL型骨牌数量:", tile)  # ==21


