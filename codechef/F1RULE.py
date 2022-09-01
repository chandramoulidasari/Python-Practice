for _ in range(int(input())):
    a,b = map(int,input().split())
    c = a/100*107
    if b <= c:
    	print("YES")
    elif b > c:
    	print("NO")
