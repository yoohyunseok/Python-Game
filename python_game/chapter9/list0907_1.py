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

neko = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0]) #append 명령으로 list 초기화

def draw_neko(): #고양이 그리기 함수
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag = "NEKO")

def yoko_neko(): #같은 고양이가 세로로 3개 놓였는지 확인하는 함수
    for y in range(10):
        for x in range(1, 7):
            if neko[y][x] >0:
                if neko[y][x-1] == neko[y][x] and neko[y][x] == neko[y][x+1]:
                    neko[y][x-1] = 7
                    neko[y][x] = 7
                    neko[y][x+1] = 7

def game_main():
    global cursor_x, cursor_y, mouse_c
    if 660 <= mouse_x and mouse_x < 840 and 100<= mouse_y and mouse_y <160 and mouse_c == 1: #풍선 안의 test를 클릭하면 yoko_neko() 실행
        yoko_neko()
    if 24 <= mouse_x and mouse_x < 24 +72 *8 and 24 <= mouse_y and mouse_y <24 + 72 * 10: #마우스가 게임 영역 내에 있을 때
        cursor_x = int((mouse_x - 24) / 72) #마우스 x 좌표로 커서 x 좌표 설정
        cursor_y = int((mouse_y - 24) / 72) #마우스 y 좌표로 커서 y 좌표 설정
        if mouse_c == 1: #클릭 한 곳에 고양이를 놓게 만드는 함수
            mouse_c = 0 #클릭 한번에 고양이 하나만 놓기
            #따로 ButtonRelease 시 실행할 함수를 설정할 필요 없이 플래그를 1에서 0으로 내려준다.
            neko[cursor_y][cursor_x] = random.randint(1, 2) 
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image = cursor, tag = "CURSOR") #3
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game_main)

root = tkinter.Tk()
root.title("가로로 3개가 나란히 놓였는가?")
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
cvs.create_rectangle(660, 100, 840, 160, fill="white")
cvs.create_text(750, 130, text="테스트", fill = "red", font = ("Times New Roman", 30))
game_main()
root.mainloop()
