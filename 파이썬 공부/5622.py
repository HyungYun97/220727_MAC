T = input()
dial = ['ABC','DEF','GHI','JKL','MNO,','PQRS','TUV','WXYZ']

first = 0 # 한번 수행하고 나면 초기값으로 돌아감.
for unit in dial: #dial 0~unit 까지 순서대로 돌아가면서 반복문이 수행된다
    for i in unit: #unit 을 반복해주는 횟수 
        for x in T:
            if i == x:  # 두 알파벳이 같으면 
                first += dial.index(unit) +3  # time = time + index +3
print(first)


# for 문 : 리스트나 튜플, 문자열의 첫번째 요소부터 마지막 요소까지 차례대로 변수에 대입. 
# 수행할 문장1, 수행할 문장2 등이 수행된다.
# 삼중 for 문을 통해 리스트 안의 각각 인덱스별로 비교하는 방법, 다시 풀어보기 