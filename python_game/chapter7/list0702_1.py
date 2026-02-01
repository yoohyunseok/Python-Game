import tkinter

def click_btn():
    text.insert(tkinter.END, "Monster is invading ") #텍스트 필드의 가장 마지막에 문자열 추가(tkinter.END)
    
root = tkinter.Tk()
root.title("여러 행  텍스트 입력 필드")
root.geometry("400x200")
button = tkinter.Button(text= "messgae", command = click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()
"""
이 예제에선 pack()으로 입력 필드를 배치했지만, place()를 사용하면
입력 필드의 배치 위치와 사이즈를 적절하게 지정 가능
ex)
text = tkinter.Text()
text.place(x = 20, y = 50, width = 360, height = 120)
"""
"""
get(시작 위치, 종료 위치)
delete(시작 위치, 종료 위치)
ex) get("1.0", "end-1c") => 입력 필드의 전체 문자열을 얻는 경우
1.0 => 1행 0번째 문자
end - 1c => 마지막(end) 위치에서 1 문자 앞이라는 뜻
"""
