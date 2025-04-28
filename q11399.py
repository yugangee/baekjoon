N = int(input())
times = sorted(map(int, input().split()))

total_time = 0
waiting_time = 0
for i in range(N):
    waiting_time += times[i]
    total_time += waiting_time

#누적합
#prefix_sum = [0] * (N + 1)  # 누적합 배열 초기화
#for i in range(1, N + 1):
#    prefix_sum[i] = prefix_sum[i - 1] + times[i - 1]

# 각 사람의 기다린 시간의 합 계산
#total_time = sum(prefix_sum)

print(total_time)