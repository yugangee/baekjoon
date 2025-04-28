import sys
input = sys.stdin.read

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

for _ in range(M):
    num1, num2 = map(int, input().split())
    sum = 0
    num1 -= 1
    num2 -= 1
    while num1 <= num2:
        sum += numbers[num1]
        num1 += 1
    print(sum)
#런타임에러