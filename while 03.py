n = int(input())

a = n
circle = 0

while(True):
    circle = circle + 1
    a = a%10*10 + (a//10 + a%10)%10
    if a == n:
        break
print(circle)