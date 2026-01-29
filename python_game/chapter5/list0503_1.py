pl_pos = 6 #플레이어의 위치 변수
def board():
    print("o"*(pl_pos - 1) + "P" + "o"*(30 - pl_pos))

board()
