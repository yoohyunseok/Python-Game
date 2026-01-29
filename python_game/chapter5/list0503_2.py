pl_pos = 6 #플레이어의 위치 변수
com_pos = 3
def board():
    print("o"*(pl_pos - 1) + "P" + "o"*(30 - pl_pos))
    print("o"*(com_pos - 1) + "C" + "o"*(30 - com_pos))

board()
