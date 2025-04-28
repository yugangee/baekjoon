# 첫째 줄에 테스트 케이스
Test = int(input())

for i in range(Test):
    n = int(input())  # n개
    clothes = {}  # 딕셔너리 생성

    # 의상 정보 받기
    for j in range(n):
        name, category = input().split()
        clothes[category] = clothes.get(category, 0) + 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)  # 해당 종류를 입거나 입지 않는 경우

    result -= 1  # 아무것도 입지 않는 경우 뺌
    print(result)
