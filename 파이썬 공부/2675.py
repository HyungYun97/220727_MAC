
#T = int(input()) # 테스트 케이스의 개수

#for _ in range(T): #int 문은 항상 range로 묶어야 가능함.
#    R,S = map(str,input().split()) # R은 반복횟수, S는 문자열
#    R = int(R)

#    for i in S:
#        P = list()
#        P[i] = R*i
#    print(P)


#2675_문자열 반복
T = int(input())


for _ in range(T):
    R, S = list(map(str, input().split()))
    R = int(R)

    for i in S:
        print(R*i, end='')
    print()