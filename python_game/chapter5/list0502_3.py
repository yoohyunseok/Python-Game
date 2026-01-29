QUESTION = [
"정현숙씨의 딸의 이름은?",
"유명호씨의 아들의 이름은?",
"정현숙씨와 유명호씨의 관계는?"] #문제 3개 리스트로 묶어서 정의
R_ANS = ["유다연", "유현석", "부부"] #정답 3개 리스트로 묶어서 정의

for i in range(3):
    print(QUESTION [i])
    ans = input()
    if ans == R_ANS[i]: #RIGHT ANSWER의 약자!
        print("정답입니다")
    else:
        print("땡!!")

#프로그램 내에서 값을 변경하지 않는 변수(상수)는 관습적으로 모두 대문자로 표기
