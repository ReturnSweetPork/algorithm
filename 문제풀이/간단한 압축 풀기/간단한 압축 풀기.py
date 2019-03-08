import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_dic = {}
    num_list = []
    for n in range(N):
        word, number = map(str, input().split())
        num = int(number)
        num_dic[word] = num

        if num_dic[word] > 10:
            num_list.append(word *10)
            num_list.append(word*(num_dic[word]-10))
        elif num_dic[word] < 10:
            num_list.append(word*(num_dic[word]))
        elif num_dic[word] == 10:
            num_list.append(word*10)
        elif num_dic[word] == 20:
            num_list.append(word * 20)

        if len(num_list[n]) == 10:
            print(num_list[n])
        elif len(num_list[n]) < 10:
            while len(num_list[n]) != 10:
                print(num_list[n])
                print(num_list[n+1])
        elif len(num_list[n]) == 20:
            print(num_list[n])
