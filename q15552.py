import sys

num = int(sys.stdin.readline())
for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

#입력이 많을 때 시간 초과를 방지하기 위해 sys.stdin.readline() 사용