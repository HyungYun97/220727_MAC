chess = [1, 1, 2, 2, 2, 8] # 체스판의 개수 

a = list(map(int,input().split())) # a 라는 변수에 리스트로 입력값을 저장한다.

for i in range(6):
    print(chess[i] - a[i], end = ' ') # 띄어쓰기가 가능하도록 end 함수를 넣어준다. 