arpa = []

with open('arpa_con.txt', 'r') as f:
	for line in f:
		arpa.append(line.replace('\n', ''))

arpa_update = []
for line in arpa:
	print(line)
	new = input("type features: ")
	arpa_update.append(line+" "+new)

print(arpa_update)
with open('arpa_con.txt', 'w') as f:
	[f.write(line) for line in arpa_update]
