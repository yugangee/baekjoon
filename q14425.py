N, M = map(int,input().split())
words = []
count = 0

for _ in range(N):
    word = input()
    words.append(word)

for _ in range(M):
    find_word = input()
    if find_word in words:
        count += 1
print(count)