a = []
location = 0

for i in range(9):
    a.append(int(input()))

for i in range(9):
    if a[i] == max(a):
        location = i+1

print(max(a))
print(location)