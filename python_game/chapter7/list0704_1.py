import tkinter
import tkinter.messagebox #메시지 박스에 사용되는 모듈 임포트

def click_btn(): #버튼 누르면 메시지 박스 띄워주는 함수
    tkinter.messagebox.showinfo("정보", "버튼을 눌렀습니다")
    
root = tkinter.Tk()
root.title("첫 번째 메시지 박스")
root.geometry("400x200")
btn = tkinter.Button(text = "test", command = click_btn)
btn.pack()
root.mainloop()
"""
메시지 박스 표시 명령
showinfo(): 정보 표시
sowwarning(): 경고 표시
showerror(): 에러 표시
askyesno(): 네, 아니오 버튼이 있는 메시지 박스
askokcancel(): ok, 취소 버튼이 있는 메시지 박스
"""
