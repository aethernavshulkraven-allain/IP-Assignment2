n = int(input("Enter the number of coordinates: "))
m = []
for i in range(n):
	tup = list(map(int, input("Enter x<space>y: ").split()))
	tup.append(1)
	m.append(tup)

s = [[0 for i in range(3)] for j in range(3)]

cx = int(input("Enter the scaling parameter (Cx): "))
cy = int(input("Enter the scaling parameter (Cy): "))
s[0][0] = cx
s[1][1] = cy 
s[2][2] = 1

#The below multiplication algo caters to all matrix multiplication cases of manner[(nx3)*(3x3)] independent of enteries
a = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
	for j in range(3):
		temp = 0
		for k in range(3):
			temp += m[i][k]*s[k][j]
		a[i][j] = temp

loc = [[a[r][c] for c in range(2)] for r in range(n)]
print("Resultant list of coordinates:\n", loc)