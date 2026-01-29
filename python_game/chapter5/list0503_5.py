import random

pl_pos = 1 #플레이어의 위치 변수
com_pos = 1
def board():
    print("o"*(pl_pos - 1) + "P" + "o"*(30 - pl_pos)+"Goal")
    print("o"*(com_pos - 1) + "C" + "o"*(30 - com_pos)+"Goal")
    
board()
print("주사위 게임 시작!")
while True:
    input("Enter를 누르면 여러분의 말이 움직입니다.") #Enter값을 받기위해 input() 사용
    pl_pos = pl_pos + random.randint(1, 6)
    if pl_pos > 30:
        pl_pos = 30
    board()
    if pl_pos == 30:
        print("여러분이 승리하셨습니다!")
        break;
    input("Enter를 누르면 컴퓨터의 말이 움직입니다.")
    com_pos = com_pos + random.randint(1, 6) #주사위 던진만큼 이동
    if com_pos > 30:
        com_pos = 30
    board()
    if com_pos == 30:
        print("컴퓨터가 승리하였습니다!")
        break;
