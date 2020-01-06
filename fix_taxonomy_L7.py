import sys

with open(sys.argv[1], "r") as f:
	for line in f:
		x = line
		y = x.count(";")
		if y < 6:
			add = 6 - y
			new = ";unknown" * add
			print(x + new)
		else:
			print(x)
			
