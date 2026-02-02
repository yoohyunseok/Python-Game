import tkinter

key = "" #key 이름 입력 변수 선언

def key_down(e): #키 눌렀을 때 실행 할 함수
    global key #나 key 끌어다쓸거임 수정도 할거임
    key = e.keysym # 눌려진 키의 이름을 key에 대입

def key_up(e): 
    global key 
    key = "" # 키를 뗐을 때 key 값 초기화

cx = 400 #캐릭터의 x 좌표 변수
cy = 300 #캐릭터의 y 좌표 변수

def main_proc():
    global cx, cy #cx, cy 전역변수 선언
    if key == "Up":  #Up 누르면
        cy = cy - 20  #y 좌표 20픽셀 감소
    if key == "Down": #Down 누르면
        cy = cy + 20 #y 좌표 20픽셀 증가
    if key == "Left": #Left 누르면
        cx = cx - 20 #x 좌표 20픽셀 감소
    if key == "Right": #Right 누르면
        cx = cx + 20 #x 좌표 20픽셀 증가
    canvas.coords("MYCHR", cx, cy) #캐릭터 이미지를 새로운 위치로 이동
    root.after(100, main_proc) #after() 메서드로 0.1초 후 실행 할 함수 설정

root = tkinter.Tk()
root.title("wong moving!!")
root.bind("<KeyPress>", key_down) #키보드를 누르면 key_down 함수 실행
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=800, height = 600, bg="lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file = "wong.png")
canvas.create_image(cx, cy, image=img, tag="MYCHR") #캔버스에 이미지 표시 
main_proc()
root.mainloop()
"""
coords("태그명", x좌표, y좌표)
캐릭터를 새로운 위치로 이동시킴

canvas.create_image(cx, cy, image = img, tag = "MYCHR")
ex) create_image() 메서드로 태그를 지정할 수 있다.
create_image의 x, y좌표는 이미지의 중심 좌표이다.

"""
