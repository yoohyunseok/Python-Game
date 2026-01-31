import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.title("첫 번째 윈도우") #제목 설정
root.geometry("800x600") #크기 설정
label = tkinter.Label(root, text="라벨 문자열", font=("System", 24)) #라벨 컴포넌트 생성
label.place(x=200, y=100) #라벨 위치 설정
root.mainloop() #윈도우 띄우기
"""
라벨 변수명 = tkinter.Label(윈도우 객체, text="라벨 문자열", font=("폰트 명", 24))
라벨 변수명.place(x=x 좌표, y= y 좌표)

"""
