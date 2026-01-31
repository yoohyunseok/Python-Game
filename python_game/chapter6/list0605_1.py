import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.title("제비 뽑기") #윈도우 제목 설정
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600) #캔버스 컴포넌트 생성
canvas.pack() #윈도우 캔버스 배치
gazou = tkinter.PhotoImage(file = "miko.png") #legend_guitar에 이미지 파일 로딩
canvas.create_image(400, 300, image = gazou) #캔버스에 이미지 그리기
root.mainloop()
