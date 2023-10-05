def courseValidity(a):
    check = False
    for k in a:
        if k.isdigit():
            check = True
            break

    if check:        
        flag1, flag2 = True, True
        for i in range(len(a)):
            if a[i].isdigit():
                letters = a[:i]
                integers = a[i:]
                break
            
        for i in letters:
            if i.isdigit():
                flag1 = False
                break
        for i in integers:
            if i.isalpha():
                flag2 = False
                break

        if flag1 and flag2:
            return True

        else:
            return False

    else:
        return False

def creditValidity(n):
    if n in "124":
        return True

    return False

def gradesValidity(x):
    lst = ['A', 'A+' , 'A-' , 'B' , 'B-' , 'C' , 'C-' , 'D' , 'F']
    if x in lst:
        return True

    return False

def inputValidity(tup):
    if len(tup) != 3:
        return False

    cond = courseValidity(tup[0]) and creditValidity(tup[1]) and gradesValidity(tup[2])

    if not cond:
        return False

    return True

def digits(s):
    num = ''
    for i in s:
        if i.isdigit():
            num += i

    return int(num)

student = []

while(True):
    s = input("Enter student details: ")

    if not s:
        break

    else:
        tup = tuple(map(str, s.split()))
        if not inputValidity(tup):
            print("Entered input is invalid!")
            forrun = False
            break

        else:
            forrun = True
            student.append(tup)

if forrun:
    sorted(student, key =lambda x: digits(x[0]))

    grade_map = {'A+':10, 'A':10, 'A-':9, 'B':8, 'B-':7, 'C':6, 'C-':5, 'D':4, 'F':2}
    prod, sum_cred = 0, 0
    for i in student:
        print(i[0], ": ", i[2])
        prod += grade_map[i[2]]*int(i[1])
        sum_cred += int(i[1])
    sgpa = prod/sum_cred

    print('SGPA:',round(sgpa,2))