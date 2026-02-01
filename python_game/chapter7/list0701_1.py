import tkinter
root = tkinter.Tk()
root.title("첫 번째 텍스트 입력 필드")
root.geometry("400x200")
entry = tkinter.Entry(width=20) # 20문자 크기짜리 1행 텍스트 입력 필드 생성
entry.place(x=10, y=10) #윈도우에 입력 필드 컴포넌트 배치
root.mainloop()
"""
GUI 컴포넌트를 만드는 메서드에 사용되는 root는 만들어지는 컴포넌트를 윈도우에
배치하는 경우에는 생략 가능
So tkinter.Entry(width=20)으로 끝남

"""
