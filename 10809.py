S = input()
#find 함수는 찾는 문자가 문자열에 없으면 -1을 출력하는 함수이다.

for i in('abcdefghijklmnopqrstuvwxyz'):
    print(S.find(i), end = ' ') # end = ' ' 개행문자 \n 이 기본적으로 들어가 있음

    # sep = ' ' -> 문자와 문자 사이에 어떤것을 출력할지 