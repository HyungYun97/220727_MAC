N = int(input()) # 26 
cnt = 0

num = N
while True: #이전의 풀었던 풀이와 같음 while True를 사용하여, 수행될 문장들을 표현함
    a = (num // 10) # 십의 자리 수를 a 라는 변수에 저장 , 2
    b = (num % 10) # 일의 자리 수를 b 라는 변수에 저장 , 6
    c = (a+b) % 10 # c는 a와 b를 더한값에 10을 나눈 나머지이다.
    num = (b*10) + c 
    
    cnt += 1
    if N == num:
        break
print(cnt)