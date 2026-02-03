import tkinter

mouse_x = 0 #마우스 포인터 x 좌표
mouse_y = 0 #마우스 포인터 y 좌표
mouse_c = 0 #마우스 포인터 클릭 여부 변수(플래그)

def mouse_move(e): #마우스 포인터 이동 시 마우스 포인터의 좌표 얻는 함수
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e): #마우스 클릭 시
    global mouse_c
    mouse_c = 1

def mouse_release(e): #마우스 클릭 후 땔 시
    global mouse_c
    mouse_c = 0

def game_main():
    fnt = ("Times New Roman", 30) #폰트 지정 변수
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c) #표시할 문자열 지정
    cvs.delete("TEST")
    cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("마우스 입력")
root.resizable(False, False)
root.bind("<Motion>", mouse_move) #마우스 움직일 때
root.bind("<ButtonPress>", mouse_press) #마우스 누를 때
root.bind("<ButtonRelease>", mouse_release) #마우스 땔 때
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
game_main()
root.mainloop()
"""
format()은 문자열 내의 {}르 변수 값으로 대체한다.
숫자를 문자열로 변환하지 않고(str()) 편리하게 사용 가능
"""
