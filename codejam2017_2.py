# program for read file
inputs = []
output = []

# you can change to small dataset
with open('B-large-practice.in','r') as file:
	for i,f in enumerate(file):
		if i is 0:
			continue
		data = int(f.rstrip('\n'))
		inputs.append(data)


for idx,number in enumerate(inputs):
	str_num = str(number)

	num_list = []
	for i,char in enumerate(str_num):
		num_list.append(int(char))
	
	for i in range(len(num_list)-1):
		if num_list[i] > num_list[i+1]:
			num_list[i] -= 1
			num_list[i+1] += 10
		
			for j in range(i,0,-1):
				if num_list[j-1] > num_list[j]:
					num_list[j-1] -= 1
					num_list[j] += 10

	number_list = []
	for i in range(len(num_list)):
		if num_list[i] > 9:
			number_list.append('9')
		elif num_list[i] is not 0:
			number_list.append(str(num_list[i]))
	output.append(''.join(number_list))

with open('output2.txt','w') as file:
	for i,num in enumerate(output):
		file.write('Case #{}: {}\n'.format(i+1,num))

print('finish')
