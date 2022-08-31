T = int(input())
for i in range(T):
	W = input().lower()
	if W=='b':
		print("Battle Ship")
	elif W=='c':
		print("Cruiser")
	elif W=='d':
		print("Destroyer")
	else:
		print("Frigate")