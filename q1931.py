n = int(input())
schedules = sorted(
    [tuple(map(int, input().split())) for _ in range(n)],
    key=lambda x: (x[1], x[0]) # 회의 종료 시간을 기준으로 정렬, 같다면 시작 시간을 기준으로 정렬. 다중정렬
)
last_meeting_time = 0
answer = 0

for start_time, end_time in schedules:
    if start_time >= last_meeting_time:
        answer += 1
        last_meeting_time = end_time

print(answer)