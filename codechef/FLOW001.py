a = int(input())
for i in range (a):
	x, y = [int(x) for x in input().split()]
	# x,y = map(int,input().split())
	print(x+y)