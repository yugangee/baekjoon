#첫째 줄에 단어의 개수 N
N = int(input())
words = []

#N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다
for i in range(N):
    w = input()
    words.append(w)

#길이가 짧은 것부터 길이가 같으면 사전 순으로
words = sorted(set(words), key=lambda x: (len(x), x))

for word in words:
    print(word)