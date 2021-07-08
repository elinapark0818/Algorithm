# n = 문서의 개수
# m =  몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    ipt = list(map(int, input().split()))
    ipt_ = [0 for i in range(n)]
    ipt_[m] = 1
    count = 0

    while True:
        if ipt[0] == max(ipt):
            count += 1
            if ipt_[0] == 1:
                print(count)
                break
            else:
                del ipt[0]
                del ipt_[0]
        else:
            ipt.append(ipt[0])
            del ipt[0]
            ipt_.append(ipt_[0])
            del ipt_[0]
