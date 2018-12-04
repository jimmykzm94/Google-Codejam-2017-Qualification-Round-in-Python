# program for read file
pancakes = []
flipper = []
output = []

# change to A-large-practice.in for large dataset
with open('A-small-practice.in','r') as file:
	for i,f in enumerate(file):
		if i is 0:
			continue
		data = f.split(' ')
		pancakes.append(data[0])
		flipper.append(int(data[1].rstrip('\n')))

# program for flipping
for idx in range(len(pancakes)):
	count = 0

	list_pancake = list(pancakes[idx])
	for index,pancake in enumerate(list_pancake):
		if pancake is '-':
			count+=1
			last_index = flipper[idx]+index
			if last_index <= len(list_pancake):
				for i in range(index,last_index):
					if list_pancake[i] is '-':
						list_pancake[i] = '+'
					else:
						list_pancake[i] = '-'	

	count_neg = 0;
	for index,pancake in enumerate(list_pancake):
		if pancake == '-':
			count_neg+=1


	if count_neg > 0:
		a = 'Case #'+str(idx+1)+': IMPOSSIBLE'
		output.append(a)
	elif count_neg is 0 and count is 0:
		a = 'Case #'+str(idx+1)+': ' + str(count)
		output.append(a)
	else:
		a = 'Case #'+str(idx+1)+': ' + str(count)
		output.append(a)

with open('output.txt','w') as file:
	for i in output:
		file.write(i + '\n')

print('finish')
