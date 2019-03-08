import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    DATE = input()
    print("#", end="")
    print(tc, end=" ")
    if int(DATE[4:6]) > 12 or int(DATE[4:6]) <= 0:
        print(-1)
    elif int(DATE[4:6]) == 1 or int(DATE[4:6]) == 3 or int(DATE[4:6]) == 5 or int(DATE[4:6]) == 7 or int(DATE[4:6]) == 8 or int(DATE[4:6]) == 10 or int(DATE[4:6]) == 12:
        if int(DATE[6:]) >31 or int(DATE[6:]) <0:
            print(-1)
        else:
            print(DATE[0:4], end="/")
            print(DATE[4:6], end="/")
            print(DATE[6:])
    elif int(DATE[4:6]) == 4 or int(DATE[4:6]) == 6 or int(DATE[4:6]) == 9 or int(DATE[4:6]) == 11:
        if int(DATE[6:]) > 30 or int(DATE[6:]) < 0:
            print(-1)
        else:
            print(DATE[0:4], end="/")
            print(DATE[4:6], end="/")
            print(DATE[6:])
    elif int(DATE[4:6]) == 2:
        if int(DATE[6:]) > 28 or int(DATE[6:]) < 0:
            print(-1)
        else:
            print(DATE[0:4], end="/")
            print(DATE[4:6], end="/")
            print(DATE[6:])


