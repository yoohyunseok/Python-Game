import random

ALP = ["A", "B", "C", "D", "E", "F", "G"]
r = random.choice(ALP)
alp = ""
for i in ALP:#range를 쓰지않고 ALP 리스트의 엘리먼트들을 i에 순차적으로 대입
    if i != r: #r이 아닌 문자열만 alp 문자열에 더해라
        alp = alp + i

print(alp)
