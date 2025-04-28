num = int(input())
for i in range(1, num + 1):
    print( " " * (num-i) + "*" * (2 * i - 1))
for i in range(1,num):
    print( " " * i + "*" * (2*num-2*i-1))
