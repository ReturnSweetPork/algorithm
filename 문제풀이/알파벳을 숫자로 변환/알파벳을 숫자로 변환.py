import sys
sys.stdin = open('input.txt', 'r')

word = (input())
for i in range(len(word)):
    print(int(ord(word[i]))-64, end=" ")