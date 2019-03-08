import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    num_dic = {}
    for i in arr:
        num_dic[i] = arr.count(i)

    res = max(list(num_dic.values()))

    print("#", end="")
    print(tc, end=" ")
    res_list = []
    for k, v in num_dic.items():
        if v == res:
            res_list.append(k)
    print(max(res_list))



