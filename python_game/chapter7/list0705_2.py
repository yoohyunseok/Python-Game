import tkinter

root = tkinter.Tk()
root.title("고양이 지수 진단 게임")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazoi = tkinter.PhotoImage(file = "mina.png")
canvas.create_image(400, 300, image=gazoi)
button = tkinter.Button(text = "진단하기", font = ("Times New Roman", 32), bg = "lightgreen")
button.place(x = 400, y = 480)
text = tkinter.Text(width = 40, height = 5, font = ("Times New Roman", 16))
text.place(x = 320, y = 30)

bvar = [None] * 7 #BooleanVar() 객체 용 리스트, [None]은 아무 것도 존재하지 않음을 의미하는 값
cbtn = [None] * 7 #체크 버튼용 리스트, 빈 상자를 준비해 뒀다고 생각하면 편함
ITEM = [ #질문 모음 리스트
    "높은 곳이 좋다",
    "공을 보면 굴리고 싶어진다",
    "깜짝 놀라면 털이 곤두선다",
    "쥐구멍이 마음에 든다",
    "개에게 적대감을 느낀다",
    "생선 뼈를 발라 먹고 싶다",
    "밤, 기운이 난다"]

for i in range(7): #체크버튼 반복 생성
    bvar[i] = tkinter.BooleanVar() #BooleanVar() 객체 생성
    bvar[i].set(False) #체크 안되있는걸로 세팅
    cbtn[i] = tkinter.Checkbutton(text = ITEM[i], font =("Times New Roman", 12), variable = bvar[i], bg = "#def")
    #체크 버튼 만들기, 배경 색 16진수로 지정#dfe
    cbtn[i].place(x = 400, y = 160+40*i) #안 겹치게 잘 배치하기
root.mainloop()
