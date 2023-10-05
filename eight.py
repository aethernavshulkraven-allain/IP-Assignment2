'''
Input file:-
3
URL00, 0.5: URL01, URL02, URL03
URL01, 0.4: URL02, URL03, URL00
URL02, 0.3: URL03, URL01, URL00
URL03, 0.8: URL04, URL05, URL00, URL01, URL02
URL04, 0.7: URL05, URL03
URL05, 0.5: URL04, URL03
'''
import re

f = open("pages.txt", "r")
n = int(f.readline().strip())
url_dict = {}
url_copy = {}
lines = f.readlines()
for l in lines:
	i, j = l.split(": ")
	key, val = i.split(", ")
	temp = {}
	temp2 = {}
	temp["init_imp"] = float(val)
	temp["links"] = re.findall(r'URL\d+', j)
	url_dict[key] = temp
	temp2["init_imp"] = 0
	temp2["links"] = re.findall(r'URL\d+', j)
	url_copy[key] = temp2


delta = 1
while(delta > 0.01):
	for k, v in url_dict.items():
		curr_imp = 0
		for d in url_dict.values():
			if k in d["links"]:
				#curr_imp += d["init_imp"]/len(d["links"])
				#print (curr_imp)
		delta = abs(v["init_imp"] - curr_imp)
		url_copy[k]["init_imp"] = curr_imp
		#print()
	url_dict = url_copy.copy()
	break

ans = list(sorted(url_dict.items(), key = lambda x: x[1]["init_imp"]))

print(f"Top {n} ranked pages are: \n")
n = -(n+1)
print(ans[-1:n:-1])