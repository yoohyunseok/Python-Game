import tkinter

def check():
    if cval.get()== True: #get() 이용해서 체크 여부 확인
        print("체크되어 있습니다")
    else:
        print("체크되어 있지 않습니다")
        
root = tkinter.Tk()
root.title("체크 상태 확인")
root.geometry("400x200")
cval = tkinter.BooleanVar() #객체 생성
cval.set(False) #객체 True로 설정
cbtn = tkinter.Checkbutton(text = "체크 버튼", variable = cval, command = check) #체크 버튼 컴포넌트 생성 + variable로
# 객체 지정해서 BooleanVar() 객체와 체크 버튼 연결
cbtn.pack() #배치
root.mainloop()
