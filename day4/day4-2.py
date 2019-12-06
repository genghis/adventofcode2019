inputrange = "124075-580769"
rangefeed = inputrange.split('-')
workinglist = [x for x in range(int(rangefeed[0]),int(rangefeed[1])+1)]

smallerlist = []
for num in workinglist:
	strungnum = str(num)
	if strungnum[0] <= strungnum[1] <= strungnum[2] <= strungnum[3] <= strungnum[4] <= strungnum[5]:
		if strungnum[0] == strungnum[1] or strungnum[1] == strungnum[2] or strungnum[2] == strungnum[3] or strungnum[3] == strungnum[4] or strungnum[4] == strungnum[5]:
			smallerlist.append(strungnum)
		else:
			pass
	else:
		pass

part2list = []
count = 0
for num in smallerlist:
	templist = []
	templist.append(num.count('1'))
	templist.append(num.count('2'))
	templist.append(num.count('3'))
	templist.append(num.count('4'))
	templist.append(num.count('5'))
	templist.append(num.count('6'))
	templist.append(num.count('7'))
	templist.append(num.count('8'))
	templist.append(num.count('9'))
	templist.append(num.count('0'))

	if 2 in templist:
		part2list.append(num)
		count += 1
	else:
		pass

print(f"Smaller list is: {count}")
