#첫째 줄에 자연수 N
N = int(input())

#다음 줄에는 N개의 정수 A[1], A[2], …, A[N]
A = set(map(int,input().split()))

#다음 줄에는 M개의 수
M = int(input())

#다음 줄에는 M(1 ≤ M ≤ 100,000)
T = map(int,input().split())

result = []
for a in T:
    if a in A:
        print(1)
    else:
        print(0)