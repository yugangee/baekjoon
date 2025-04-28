#첫째 줄에 온라인 저지 회원의 수 N
N = int(input())
member = [] #리스트 생성

#둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분, 튜플로 저장
for i in range(N):
    age, name = input().split()
    age = int(age)
    member.append((age, name)) #튜플형태로 member리스트에 추가

#나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서
member.sort(key=lambda x: x[0]) #오름차순 정렬

for age, name in member:
    print(age, name)