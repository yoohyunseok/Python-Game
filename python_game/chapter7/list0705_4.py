import tkinter

RESULT = [
    "전생에 고양이었을 가능성은 매우 낮습니다.",
    "보통 사람입니다.",
    "특별히 이상한 곳은 없습니다.",
    "꽤 고양이 다운 구석이 있습니다.",
    "고양이와 비슷한 성격 같습니다.",
    "고양이와 근접한 성격입니다.",
    "전생에 고양이었을지도 모릅니다.",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]

def click_btn():
    pts = 0 #체크한 버튼 수 확인 변수
    for i in range(7):
        if bvar[i].get() == True: #체크 여부 확인
            pts = pts + 1 #체크되어 있으면 +1
    nekodo = int(100*pts/7)
    text.delete("1.0", tkinter.END) #입력 필드 문자열 삭제
    text.insert("1.0", "<진단 결과> \n당신의 고양이 지수는 "+str(nekodo) + "% 입니다.\n" + RESULT[pts]) #입력 필드에 숫자값 대입
        
root = tkinter.Tk()
root.title("고양이 지수 진단 게임")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazoi = tkinter.PhotoImage(file = "mina.png")
canvas.create_image(400, 300, image=gazoi)
button = tkinter.Button(text = "진단하기", font = ("Times New Roman", 32), bg = "lightgreen", command=click_btn)
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
