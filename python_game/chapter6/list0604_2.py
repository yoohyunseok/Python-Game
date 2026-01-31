import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.title("첫 번째 캠버스") #윈도우 제목 설정
canvas = tkinter.Canvas(root, width=1000, height=600, bg="skyblue") #캔버스 컴포넌트 생성
canvas.pack() #윈도우 캔버스 배치
legend_guitar = tkinter.PhotoImage(file = "레전드 기타.png") #legend_guitar에 이미지 파일 로딩
canvas.create_image(500, 300, image = legend_guitar) #캔버스에 이미지 그리기
root.mainloop()
"""
캔버스 변수명.create_image(x 좌표, y 좌표, image = 이미지를 로딩한 변수)
여기서 x 좌표, y 좌표는 이미지의 중점의 좌표임

이미지 로딩할 변수명 = tkinter.PhotoImage(file = "파일 명.확장자")

"""
