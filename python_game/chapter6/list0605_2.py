import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.title("제비 뽑기") #윈도우 제목 설정
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600) #캔버스 컴포넌트 생성
canvas.pack() #윈도우 캔버스 배치
gazou = tkinter.PhotoImage(file = "miko.png") #legend_guitar에 이미지 파일 로딩
canvas.create_image(400, 300, image = gazou) #캔버스에 이미지 그리기
label = tkinter.Label(root, text="??", font=("Times New Roman", 120), bg = "white") #라벨 컴포넌트 생성
label.place(x=380, y=60) #라벨 위치 설정
button = tkinter.Button(root, text = "제비 뽑기", font = ("Times New Roman", 36), fg="skyblue") #버튼 컴포넌트 생성, 문자열 색상 fg로 설정
button.place(x=360, y=400) # 윈도우에 버튼 배치
root.mainloop()
