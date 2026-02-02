import tkinter

key = 0 #key 코드 입력 변수 선언

def key_down(e): #키 눌렀을 때 실행 할 함수
    global key #나 key 끌어다쓸거임 수정도 할거임
    key = e.keycode # 눌려진 키의 코드를 key에 대입

def main_proc():
    label["text"]=key
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("실시간 키 입력")
root.bind("<KeyPress>", key_down) #키보드를 누르면 key_down 함수 실행
label = tkinter.Label(font =("Times New Roman", 80))
label.pack()
main_proc()
root.mainloop()
