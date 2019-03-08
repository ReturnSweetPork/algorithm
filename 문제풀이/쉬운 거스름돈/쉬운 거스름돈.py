import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cnt50000 = 0
    cnt10000 = 0
    cnt5000 = 0
    cnt1000 = 0
    cnt500 = 0
    cnt100 = 0
    cnt50 = 0
    cnt10 = 0
    money = (int(input())//10)*10
    while money != 0:
        if money >= 50000:
            cnt50000 = money//50000
            money -= 50000*cnt50000
        elif money >= 10000:
            cnt10000 = money//10000
            money -= 10000*cnt10000
        elif money >= 5000:
            cnt5000 = money//5000
            money -= 5000*cnt5000
        elif money >= 1000:
            cnt1000 = money//1000
            money -= 1000*cnt1000
        elif money >= 500:
            cnt500 = money//500
            money -= 500*cnt500
        elif money >= 100:
            cnt100 = money//100
            money -= 100*cnt100
        elif money >= 50:
            cnt50 = money//50
            money -= 50*cnt50
        elif money >= 10:
            cnt10 = money//10
            money -= 10*cnt10
    print("#", end="")
    print(tc)
    print(cnt50000, cnt10000, cnt5000, cnt1000, cnt500, cnt100, cnt50, cnt10)
