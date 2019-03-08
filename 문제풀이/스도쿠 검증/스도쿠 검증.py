import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for x in range(9)]
    check = [1,2,3,4,5,6,7,8,9]
    flag1 = 0
    flag2 = 0
    flag3 = 0
    for x in range(9):
        if sorted(arr[x]) != check:
            flag1 =1
            break
    col_arr = []
    for x in range(9):
        for y in range(9):
            col_arr.append(arr[y][x])
        if sorted(col_arr) != check:
            flag2 =1
            break
        col_arr = []

    for x in range(9):
        for y in range(9):
            three_arr=[]
            if x%3 == 0 and y%3 == 0:
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        three_arr.append(arr[i][j])

                if sorted(three_arr) != check:
                    flag3 = 1
                    break
    print("#", end="")
    print(tc, end=" ")
    if flag1 == 1 or flag2 ==1 or flag3 == 1:
        print(0)
    else:
        print(1)