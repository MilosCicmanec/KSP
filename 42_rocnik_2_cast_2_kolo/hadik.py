inputs = [int(i) for i in input().split()]
m , n = inputs[0], inputs[1]

moves = list(input())

x,y= 0,0
min_x = min_y = max_y = max_x = 0
visited = set()
visited.add((x,y))

for move in moves:
    if move == "H":
        y+=1
    elif move == "D":
        y-=1
    elif move == "L":
        x-=1
    else:
        x+=1
    if (x,y) in visited:
        print(0)
        exit()
    visited.add((x,y))
    min_x = min(x,min_x)
    min_y = min(y,min_y)
    max_x = max(x,max_x)
    max_y = max(y,max_y)

a = abs(min_x-max_x) +1
b = abs(min_y-max_y) +1

if a > m or b > n:
    print(0)
else:
    print((m-a+1)*(n-b+1))
