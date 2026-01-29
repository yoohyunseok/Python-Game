import random
cnt = 0
while True: #while문 무한 반복
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break; #while문 탈출 

print(str(cnt)+" 번째만에 드디어 뽑았다") #int -> str 형변환 숫자와 문자열을 연결하기위해
