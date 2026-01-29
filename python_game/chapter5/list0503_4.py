import random

pl_pos = 1 #플레이어의 위치 변수
com_pos = 1
def board():
    print("o"*(pl_pos - 1) + "P" + "o"*(30 - pl_pos))
    print("o"*(com_pos - 1) + "C" + "o"*(30 - com_pos))

while True:
    board()
    input("Enter를 누르면 말이 움직입니다") #Enter값을 받기위해 input() 사용
    pl_pos = pl_pos + random.randint(1, 6)
    com_pos = com_pos + random.randint(1, 6) #주사위 던진만큼 이동
