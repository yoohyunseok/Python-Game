import tkinter

def click_btn():
    button["text"] = "You clicked!" #버튼 문자열 변경
    
root = tkinter.Tk() #root라는 윈도우 객체 생성
root.title("첫 번째 윈도우") #제목 설정
root.geometry("800x600") #크기 설정
button = tkinter.Button(root, text = "버튼 문자열", font = ("Times New Roman", 24), command = click_btn) #버튼 컴포넌트 생성, command 이용해서 클릭 시 동작할 함수 지정
button.place(x=200, y=100) # 윈도우에 버튼 배치
root.mainloop()
