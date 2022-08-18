word = input().lower() # 주어지는 단어 소문자로 변환시킨다.
word_list = list(set(word)) # 입력받은 단어값을 중복 제거 후 리스트형태로 저장 
cnt = [] # cnt 라는 리스트를 생성하고, 거기에 같은 알파벳이 몇 번 나오는지 확인해야함

for i in word_list:
    count = word.count(i) # count 의 m,i,s,p 0번째부터 순서대로 확인할 수 있어서 count(i)가 맞음
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(word_list[cnt.index(max(cnt))].upper())