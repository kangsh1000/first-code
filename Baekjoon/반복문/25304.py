x = int(input())
y = int(input())
count = 0
total = 0
for i in range(1, y+1):
    A,B = map(int,input().split())
    count = A * B
    total += count


if total == x:
    print("Yes")

else:
    print("No")

    