from random import randint

print("nhap dam la keo")
player = input()
computer = randint(0,2)


if computer == 0:
	computer = "Bua"
if computer == 1:
	computer = "Bao"
if computer == 2:
	computer = "Keo" 

print("_ _ _")
print("Your choose: " + player)
print("Computer chooses: "+ computer)
print("_ _ _")
if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Bua":
			print("Lose")
		else:
			print("Win")

	elif player == "Bao":
		if computer == "Keo":
			print("Lose")
		else:
			print("Win")

	elif player == "Bua":
		if computer == "Bao":
			print("Lose")
		else:
			print("Win")
	else: 
		print("nhap lai con trai")