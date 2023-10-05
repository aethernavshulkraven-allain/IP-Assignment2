f = open("fileforq3.txt","r")
s = '''
'''
n = 0
for l in f:
	if ":" in l:
		n+=1
		continue
	elif "..." in l: continue
	else: s+=l

f.close()
f = open("fileforq3.txt", "w")
f.write(s.strip())
f.close()
f = open("fileforq3.txt", "r")
yearbook = {}
for i in range(1,n+1):
	key = "name"+str(i)
	val = ''
	for j in range(n-1):
		val += f.readline() + ""
	yearbook[key] = val

for k,v in yearbook.items():
	print(k,":")
	print(v)
print()

countmax = -1
countmin = 10000000000
maxi = ''
for i, j in yearbook.items():
	if j.count(", 1") > countmax:
		countmax = j.count(", 1")
		maxi = str(i)
	elif j.count(", 1") == countmax:
		countmax = j.count(", 1")
		maxi += str(i) + " "

mini = ''
for i, j in yearbook.items():
	if j.count(", 1") < countmin:
		countmin = j.count(", 1")
		mini = str(i)
	elif j.count(", 1") == countmin:
		countmin = j.count(", 1")
		mini += " " + str(i)

print(maxi, "Has the maximum number of signs and", mini , "has the minimum number of signs")
print("\nTHE INPUT FILE IS CHANGED, RUN AGAIN KINDLY RESET THE FILE")