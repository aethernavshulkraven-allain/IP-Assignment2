menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
menu_dict = dict(menu)

i = 1
for a, b in menu_dict.items():
    print(i, a, b)
    i+=1

lst_keys = list(menu_dict.keys())
lst_keys.insert(0, 0)

print("Please enter item number and quantity of item")

order = {}

while (True):
	s = input()

	if not s:
		break

	else:
		x,y = map(int, s.split())
		order[x] = y

print("--------------Your order--------------")
total = 0
for i,j in order.items():
	total += (menu_dict[lst_keys[i]])*j
	print(lst_keys[i], ", ", j, ", Rs ",(menu_dict[lst_keys[i]])*j)

lst_qty = list(order.values())
t_qty = sum(lst_qty)
print("TOTAL", ", ", t_qty," items",", Rs ",total)
print("--------------Thanks For Ordering!--------------")