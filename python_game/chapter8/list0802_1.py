import tkinter
key = 0 #key 코드 입력 변수 선언
def key_down(e): #키 눌렀을 때 실행 할 함수
    global key #나 key 끌어다쓸거임 수정도 할거임
    key = e.keycode # 눌려진 키의 코드를 key에 대입
    print("KEY:" +str(key)) #쉘 윈도우에 키 값 출력

root = tkinter.Tk()
root.title("키 코드 얻기")
root.bind("<KeyPress>", key_down) #키보드를 누르면 key_down 함수 실행
root.mainloop()
"""
bind("<이벤트>", 이벤트 발생 시 실행 할 함수명)

주요 이벤트
<KeyPress> or <Key> : 키를 누름
<KeyRelease> : 키를 눌렀다 뗌
<Motion> : 마우스 포인터 움직임
<ButtonPress> or <Button> : 마우스 버튼 클릭

@@@<ButtonPress>는 마우스의 모든 버튼 감지
<Button-1> : 좌 클릭
<Button-2> : 휠 클릭
<Button-3> : 우 클릭 감지

"""
