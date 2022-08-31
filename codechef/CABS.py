n = int(input())
for i in range(n):
	a,b=map(int,input().split())
	if a < b:
		print("First")
	elif b < a:
		print("Second")
	else:
		print("Any")