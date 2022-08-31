A = ['Kid Milli','Loopy','Han Yo Han', 'Changmo']

n = int(input())


for i in range(n):
    B = (A[0:i])
print(B)


# for문을 활용, n 에 상수를 입력받고, 입력받은 횟 수 만큼 반복해서 출력해준다.
# B 에 A[i] 값을  넣으면, i 번째 마지막으로 나오는 리스트의 A 값을 입력받게 된다.
# 리스트에 A[0:N] 0번째부터 N번째까지 출력하게 된다. 