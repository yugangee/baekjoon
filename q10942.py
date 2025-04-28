N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
questions = []
for _ in range(M):
    start, end = map(int, input().split())
    questions.append((start, end))

for start, end in questions:
    start -= 1
    end -= 1
    palindrome = True
    while start < end:
        if numbers[start] != numbers[end]:
            palindrome = False
            break
        start += 1
        end -= 1
    if palindrome:
        print(1)
    else:
        print(0)