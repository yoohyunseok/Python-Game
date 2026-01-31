import tkinter

root = tkinter.Tk() #윈도우 객체 생성
root.title("첫 번째 캠버스") #윈도우 제목 설정
canvas = tkinter.Canvas(root, width=400, height=600, bg="skyblue") #캔버스 컴포넌트 생성
canvas.pack() #윈도우 캔버스 배치
root.mainloop()
"""
pack() 메서드로 캔버스를 윈도우에 배치하면 캔버스 크기에 맞춰 윈도우 크기가 결정된다.
그래서 이 예제에 geometry() 메서드 사용 안함

"""
"""
캔버스 변수 명 = tkinter.Canvas(윈도우 객체명, width=너비, height=높이, bg="배경색") #캔버스 컴포넌트 생성
캔버스 변수 명.pack()

"""
