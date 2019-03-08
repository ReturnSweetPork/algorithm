import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
cnt = 0
for i in range(1, n+1):
    num = str(i)

    for j in range(len(num)):
        if num[j] == '3' or num[j] =='6' or num[j] == '9':
            cnt +=1

    if cnt != 0:
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ")
    cnt = 0
