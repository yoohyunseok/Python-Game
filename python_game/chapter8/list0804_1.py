import tkinter
root = tkinter.Tk()
root.title("미로 표시")
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()
maze = [ #미로 구조(1이 벽, 0이 길)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill="gray")
            #create_rectangle()로 사각형을 그린다.
root.mainloop()
"""
python은 C와 다르게 [행][열] 이라서
이중 for 문도 헷갈리지 말라고 y 반복문 안에 x 반복문을 돌리는구나
"""
