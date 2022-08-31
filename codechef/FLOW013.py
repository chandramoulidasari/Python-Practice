T = int(input())
for i in range(T):
	a,b,c = map(int,input().split())
	d = a+b+c
	if d==180:
		print("YES")
	else:
		print("NO")