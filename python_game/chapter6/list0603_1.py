import tkinter

root = tkinter.Tk() #root라는 윈도우 객체 생성
root.title("첫 번째 윈도우") #제목 설정
root.geometry("800x600") #크기 설정
button = tkinter.Button(root, text = "버튼 문자열", font = ("Times New Roman", 24)) #버튼 컴포넌트 생성
button.place(x=200, y=100) # 윈도우에 버튼 배치
root.mainloop()
"""
버튼 변수명 = tkinter.Button(윈도우 객체, text = "버튼 문자열", font = ("폰트 명", 24)) 
버튼 변수명.place(x=x 좌표, y=y 좌표)

"""
