N, K = map(int, input().split())
number = input()
stack = []

for digit in number:
    stack.append(int(digit)) #스택에 넣기

for _ in range (K):
    for i in range(N):
        if stack and stack[-1] < i: #앞에 숫자가 더 작으면 제거
            stack.pop(stack[-1])
        else:
            pass

result = ''.join(map(str, stack)) #합쳐서 출력
print(result)