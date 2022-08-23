from ast import Num


T = int(input())

for _ in range(T):
    k = int(input()) # k = 층
    n = int(input()) # n = 호수

    apt = [i for i in range(1,n+1)] # conprehension 으로 쉽게 표현함.
    # 1부터 입력받은 숫자의 범위까지 1+i 반복한 리스트를 생성해준다.

    for _ in range(k):
        for j in range(1,n): # 이중 반복문을 통해서, 층수까지 다 반복 시키고, 마지막 호수를 출력하도록 설정
            apt[j] += apt[j-1]
    print(apt[-1])

    #https://elrion018.tistory.com/24
    #https://ooyoung.tistory.com/89 
    # 한번 더 이해하기 
