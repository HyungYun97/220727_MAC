T = int(input()) # 테스트 케이스의 개수


for i in range(T): #int 문은 항상 range로 묶어야 가능함.
    R,S = map(str,input().split()) # R은 반복횟수, S는 문자열
    R = int(R)

    for i in range(R):
        S = R * i

    print(S)