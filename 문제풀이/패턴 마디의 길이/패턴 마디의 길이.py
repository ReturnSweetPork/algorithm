import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    word = input()
    wordlist = []
    for i in range(30):
        if word[0:i] == word[i:2*i]:
            wordlist.append(word[0:i])
    print("#", end="")
    print(tc, end=" ")
    print(len(wordlist[1]))
