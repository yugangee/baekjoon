N, M = map(int, input().split())
words = []
for _ in range(N):
    words.append(input())
check_list = []
for _ in range(M):
    check_list.append(input())

cnt = 0
for word in check_list:
    if word in words:
        cnt += 1

print(cnt)