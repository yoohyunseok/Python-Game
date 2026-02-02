import tkinter

tmr = 0 #type : int
def count_up():
    global tmr #함수 외부의 tmr 변수 끌어다쓰기
    tmr = tmr + 1
    label["text"] = tmr #label 객체의 text를 tmr로 바꿔서 화면에  초 띄우기
    root.after(1000, count_up) #재귀 호출

root = tkinter.Tk()
label = tkinter.Label(font = ("Times New Roman", 80))
label.pack()
root.after(1000, count_up) #after()로 실시간 처리
root.mainloop()
"""
after(밀리 초, 실행 할 함수명)

global은 함수 밖에서 정의한 변수 값을 함수 안에서 변경할 때 사용

"""
