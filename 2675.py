#R = int(input())
#
#for i in range(R):
#    S,P = input().split()
#    S = int(S)
#    P = str(P) # P는 문자열 S는 숫자형이므로 무조건 int, str 로 받으면 안된다. 
#    for i in range(len(S)):
#        print(S*P[i],end='')
#    print()


n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김