# 반복문 사용 시, 몇 번째 반복문인지 확인이 필요할 때 사용합니다.
# 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환합니다.

ex = [53, 16, 890, 324, 3, 77]
for i in enumerate(ex):
    print(i)

for i, v in enumerate(ex):
    print("index : {}, value: {}".format(i, v))
