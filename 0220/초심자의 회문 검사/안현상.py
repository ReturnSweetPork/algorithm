import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    word = input()
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])
    res = 0
    for i in range(len(word_list)//2):
        if word_list[i] != word_list[len(word_list) -i -1]:
            res += 1

    print(f"#{tc}" ,end=" ")
    if res != 0:
        print(0)
    else:
        print(1)


