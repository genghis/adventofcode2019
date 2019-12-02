pairs = [(x,y) for x in range(100) for y in range(100)]

for pair in pairs:
	inputlist = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0]
	noun = pair[0]
	verb = pair[1]
	inputlist[1] = noun
	inputlist[2] = verb
	opcode_position = 0

	def opcode1(num1, num2, num3):
		inputlist[num3] = inputlist[num1] + inputlist[num2]

	def opcode2(num1, num2, num3):
		inputlist[num3] = inputlist[num1] * inputlist[num2]

	while True:
		firstnumber = inputlist[(opcode_position+1)]
		secondnumber = inputlist[(opcode_position+2)]
		thirdnumber = inputlist[(opcode_position+3)]
		if inputlist[opcode_position] == 1:
			opcode1(firstnumber, secondnumber, thirdnumber)
			opcode_position += 4
		elif inputlist[opcode_position] == 2:
			opcode2(firstnumber, secondnumber, thirdnumber)
			opcode_position += 4
		elif inputlist[opcode_position] == 99:
			break
		else:
			print("You fucked up.")

	if inputlist[0] == 19690720:
		print(f"{noun} is noun and {verb} is verb")
		adventanswer = (100 * noun) + verb
		print(f"Advent answer is {adventanswer}")
		break
	else:
		pass
