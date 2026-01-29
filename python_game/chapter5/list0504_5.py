import random
import datetime
ALP = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]
r = random.choice(ALP)
alp = ""
for i in ALP:#range를 쓰지않고 ALP 리스트의 엘리먼트들을 i에 순차적으로 대입
    if i != r: #r이 아닌 문자열만 alp 문자열에 더해라
        alp = alp + i

print(alp)
st = datetime.datetime.now() #문제 시작 시간 check
ans = input("빠진 알파벳은? ")
if ans == r:
    print("정답입니다")
    et = datetime.datetime.now() #문제 푼 시간 check
    print(str((et- st).seconds)+" 초 걸렸습니다") #et와 st의 차이를 초단위로 출력
else:
    print("틀렸습니다")
