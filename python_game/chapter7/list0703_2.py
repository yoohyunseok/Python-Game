import tkinter
root = tkinter.Tk()
root.title("처음부터 체크된 상태 만들기")
root.geometry("400x200")
cval = tkinter.BooleanVar() #객체 생성
cval.set(True) #객체 True로 설정
cbtn = tkinter.Checkbutton(text = "체크 버튼", variable = cval) #체크 버튼 컴포넌트 생성 + variable로
# 객체 지정해서 BooleanVar() 객체와 체크 버튼 연결
cbtn.pack() #배치
root.mainloop()
