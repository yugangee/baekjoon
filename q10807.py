num = int(input())
a = list(map(int, input().split()))
find_num = int(input())

answer = 0
for i in range(num):
    if a[i] == find_num:
        answer += 1

print(answer)
