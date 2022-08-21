A,B = input().split()
reverseA = int(A[::-1])
reverseB = int(B[::-1])

if reverseA > reverseB:
    print(reverseA)

else:
    print(reverseB)


# 리스트를 사용하지 않은 단순 숫자형 문자들의 역순을 계산해서 풀이한 답안

# 파이썬의 역순을 계산하기 위해서는 [::-1] 을 사용해주면 된다. 