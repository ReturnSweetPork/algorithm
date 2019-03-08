import sys
sys.stdin = open('input.txt', 'r')
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
T = int(input())
for tc in range(1,T+1):
    S, N = map(int, input().split())
    student = []
    for n in range(S):
        M, L, Q = map(int, input().split())
        score = (M*0.35)+(L*0.45)+(Q*0.2)
        student.append(score)
        student2 = list(reversed(sorted(student)))
        student2.insert(0,0)
    res = (student2.index(student[N-1]))-1
    print("#", end="")
    print(tc, end=" ")

    print(grade[(res//(S//10))])