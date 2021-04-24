# 입력된 문자를 모두 대문자로 변환하기
a = input().upper()

# a의 중복값을 제외한 문자들을 only_words 에 리스트로 만들어 담기
only_words = list(set(a))

# 문자를 count 하고 count된 숫자를 리스트에 추가하기
count_list = []
for x in only_words:
    count = a.count(x)
    count_list.append(count)

# count 된 문자의 최대 개수가 같은 다른 문자가 있다면 ? 출력하기
if count_list.count(max(count_list)) > 1:
    print("?")
# count 된 문자의 최대값 위치 찾아서 출력하기
else:
    max_index = count_list.index(max(count_list))
    print(only_words[max_index])