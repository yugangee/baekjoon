N= int(input())
nums = list(map(int, input().split()))


current_num = 0 #최근 처치 수
highest = 0 #가장 높은 봉우리
max_num = 0

for i in range(N):
    if nums[i] > highest: #현재 봉우리가 더 크면 0으로 초기화
        highest = nums[i]
        current_num = 0
    else: #현재 봉우리가 전보다 작아서 처치 가능 +1
        current_num += 1

    max_num = max(current_num, max_num)

print(max_num)