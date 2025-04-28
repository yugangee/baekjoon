#n: 바구니 개수, m:공을 넣는 횟수
n,m = map(int, input().split())

#바구니 배열 만들기
#값이 없는 인덱스를 직접 지정해서 대입하면 오류가 남
#0으로 초기화 해야됨
basket = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        basket[a] = k

for i in range(n):
    print(basket[i],end=" ")