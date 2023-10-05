

contacts = {}

#num_contacts = int(input("Enter how many contacts would you like to add to contact book: "))

'''
for i in range(num_contacts):
	det = {}
	temp = []
	name = input("Enter the name of the contact: ")
	if name not in contacts.keys(): contacts[name] = temp
	det["Address"] = input("Enter the address of the contact: ")
	det["Phone"] = int(input("Enter the number of the contact: "))
	det["email"] = input("Enter the email-id of the contact: ")
	contacts[name].append(det)'''

cont_str = str(contacts).strip("{").strip("}")
open("addrbook.txt", "w").close()
f = open("addrbook.txt", "w")
f.write(cont_str)
f.close()

print('''\nList of operations:- 
	1. Insert a new entry
	2. Delete an entry
	3. Find matching entries
	4. Email
	5. Phone
	6. exit\n

	*** IMPORTANT:- DO EXIT TO SAVE CHANGES TO DIRECTORY!! i.e. do pass operation 6 before closing ***''')



will = True
while(will):
	op = int(input("\nWhat do you want to do?(Enter index number of operation): "))
	if op == 1:
		det = {}
		temp = []
		name = input("Enter the name of the contact: ")
		if name not in contacts.keys(): contacts[name] = temp
		det["Address"] = input("Enter the address of the contact: ")
		det["Phone"] = int(input("Enter the number of the contact: "))
		det["email"] = input("Enter the email-id of the contact: ")
		contacts[name].append(det)

	elif op == 2:
		k = input("Enter the name of the contact: ")
		if k in contacts.keys() and len(contacts[k])>1:
			print(contacts[k])
			contacts[k].pop(int(input("Enter the no. of data which you want to delete: ")))
		elif k not in contacts.keys():
			print("Contact not found!")
		else:
			del contacts[k]

	elif op == 3:
		for i in contacts.keys():
			if input("Enter the partial name: ") in i:
				print(i, " : ", contacts[i])

	elif op == 4:
		k = input("Enter the name of the contact: ")
		if k in contacts.keys():
			for i in contacts[k]:
				print(i["email"])
		else:
			print("Not found!")

	elif op == 5:
		k = input("Enter the name of the contact: ")
		if k in contacts.keys():
			for i in contacts[k]:
				print(i["Phone"])
		else:
			print("Not found!")

	else:
		cont_str = str(contacts).strip("{").strip("}")
		open("addrbook.txt", "w").close()
		f = open("addrbook.txt", "w")
		f.write(cont_str)
		f.close()
		break

	if input("Anything else?(Y/N): ") == "Y": will = True
	else: will = False
