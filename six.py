#we will solve this problem considering 10 students
wts = [(30, 20), (50, 20), (100, 40), (50, 20)]#4 assignments
m = []
total_marks = 0
f1 = open("/Users/arnavshukla/Documents/IIITD/IP/IP-ASSIGNMENT2/IPmarks.txt", "r")
f2 = open("/Users/arnavshukla/Documents/IIITD/IP/IP-ASSIGNMENT2/IPgrades.txt", "w")
for i in range(10):
	total_marks = 0
	roll = f1.readline(2)
	s = f1.readline()
	m = list(map(int, s[2:].split(", ")))
	for j in range(4):
		total_marks += (m[j]/wts[j][0])*wts[j][1]

	if total_marks > 80:
		grade = "A"
	elif total_marks > 70:
		grade = "A-"
	elif total_marks > 60:
		grade = "B"
	elif total_marks > 50:
		grade = "B-"
	elif total_marks > 40:
		grade = "C"
	elif total_marks > 35:
		grade = "C-"
	elif total_marks > 30:
		grade = "D"
	else:
		grade = "F"

	rep = f"{roll}, {total_marks}, {grade}\n"
	f2.write(rep)