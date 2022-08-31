n = int(input())
for i in range(n):
	a,b=map(int,input().split())
	if a > b:
		print(a - b)
	elif b > a:
		print(b - a)
	else:
		print(a-b)
	# or
	print(abs(a-b))