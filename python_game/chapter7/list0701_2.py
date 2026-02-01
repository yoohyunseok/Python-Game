import tkinter

def click_btn():
    txt = entry.get() #텍스트 필드 entry에 입력된 문자열 얻기
    button["text"] = txt #button의 텍스트 매개변수의 값 변경
    
root = tkinter.Tk()
root.title("첫 번째 텍스트 입력 필드")
root.geometry("400x200")
entry = tkinter.Entry(width=20) # 20문자 크기짜리 1행 텍스트 입력 필드 생성
entry.place(x=20, y=20) #윈도우에 입력 필드 컴포넌트 배치
button = tkinter.Button(text= "get string", command = click_btn)
button.place(x=20, y=100)
root.mainloop()
#entry 내 문자열 삭제 => delete(), entry 내 문자열 삽입=>insert()
