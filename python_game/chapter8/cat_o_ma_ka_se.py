import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(400, 300, image=photo[pnum], tag="PH")
    pnum = pnum + 1
    if pnum >= len(photo): #입력한 사진(elemnet) 수 얻기
        pnum = 0 #마지막 이미지 표시 후 다시 처음 사진으로 돌아가기
    root.after(7000, photograph)

root = tkinter.Tk()
root.title("디지털 액자")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
photo = [
    tkinter.PhotoImage(file="cat00.png"),
    tkinter.PhotoImage(file="cat01.png"),
    tkinter.PhotoImage(file="cat02.png"),
    tkinter.PhotoImage(file="cat03.png")
]
photograph()
root.mainloop()
