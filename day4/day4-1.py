inputrange = "124075-580769"
rangefeed = inputrange.split('-')
workinglist = [x for x in range(int(rangefeed[0]),int(rangefeed[1])+1)]

count = 0
for num in workinglist:
	strungnum = str(num)
	if strungnum[0] <= strungnum[1] <= strungnum[2] <= strungnum[3] <= strungnum[4] <= strungnum[5]:
		if strungnum[0] == strungnum[1] or strungnum[1] == strungnum[2] or strungnum[2] == strungnum[3] or strungnum[3] == strungnum[4] or strungnum[4] == strungnum[5]:
			count += 1
		else:
			pass
	else:
		pass

print(f"{count} numbers meet the criteria")