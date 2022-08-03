#rock paper scissors game
import random

def is_win(me,pc):
	if me=='r' and pc=='s' or me=='s' and pc=='p' or me=='p' and pc=='s':
		return True
	else:
		return False	

ans = ['r','p','s']
yours = input("Enter r for rock, p for paper, s for scissors...\n")
computer_guess = random.choice(ans)
print(computer_guess)
if is_win(yours,computer_guess):
	print("Yaay!!you've won")
else:
	print("Yaay!! I've won")