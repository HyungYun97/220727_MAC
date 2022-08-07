from calendar import c


X = int(input()) # 영수증의 총 금액
N = int(input()) # 영수증에 적힌 물건의 수
Z = 0 # 총 금액과 비교할 값

for i in range(N):
    a,b = map(int,input().split())
    c = 0
    c = (a*b)
    Z += c

if Z == X:
    print("YES")
else:
    print("NO")