import tkinter
root = tkinter.Tk()
root.title("체크 버튼 다루기")
root.geometry("400x200")
cbtn = tkinter.Checkbutton(text = "체크 버튼") #체크 버튼 컴포넌트 생성
cbtn.pack() #배치
root.mainloop()
