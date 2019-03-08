import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    check = ['0','1','2','3','4','5','6','7','8','9']
    num_list = []
    cnt = 1
    res = []
    print("#", end="")
    print(tc, end=" ")
    while True:
        str_num = str(num*cnt)
        for i in str_num:
            res.append(i)
        res2 = sorted(set(res))

        if res2 == check:
            print(str_num)
            break
        else:
            cnt += 1



