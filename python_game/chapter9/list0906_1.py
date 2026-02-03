import tkinter
import random

cursor_x = 0 #커서 x 좌표
cursor_y = 0 #커서 y 좌표
mouse_x = 0 #마우스 포인터 x 좌표
mouse_y = 0 #마우스 포인터 y 좌표
mouse_c = 0 #마우스 포인터 클릭 여부 변수(플래그)

def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e): #마우스 클릭 시
    global mouse_c
    mouse_c = 1

neko = [ #고양이 위치를 관리할 2차워 리스트
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def draw_neko(): #고양이 그리기 함수
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag = "NEKO")

def drop_neko(): #고양이 낙하시키는 함수
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

def game_main():
    global cursor_x, cursor_y, mouse_c
    drop_neko()
    if 24 <= mouse_x and mouse_x < 24 +72 *8 and 24 <= mouse_y and mouse_y <24 + 72 * 10: #마우스가 게임 영역 내에 있을 때
        cursor_x = int((mouse_x - 24) / 72) #마우스 x 좌표로 커서 x 좌표 설정
        cursor_y = int((mouse_y - 24) / 72) #마우스 y 좌표로 커서 y 좌표 설정
        if mouse_c == 1: #클릭 한 곳에 고양이를 놓게 만드는 함수
            mouse_c = 0 #클릭 한번에 고양이 하나만 놓기
            #따로 ButtonRelease 시 실행할 함수를 설정할 필요 없이 플래그를 1에서 0으로 내려준다.
            neko[cursor_y][cursor_x] = random.randint(1, 6) 
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image = cursor, tag = "CURSOR") #3
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game_main)

root = tkinter.Tk()
root.title("클릭해서 고양이 놓기")
root.resizable(False, False)
root.bind("<Motion>", mouse_move) #마우스 움직일 때
root.bind("<ButtonPress>", mouse_press) #마우스 누를 때
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
bg = tkinter.PhotoImage(file = "neko_bg.png")
cursor = tkinter.PhotoImage(file = "neko_cursor.png")
img_neko = [ #고양이 이미지 파일 모음 리스트
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
]

cvs.create_image(456, 384, image=bg)
game_main()
root.mainloop()
