#random number guess game
import random

def our_guess(high):
	guess = int(input(f"Enter your number b/w 0 and {high}\n"))
	correct = random.randint(0,high)
	while guess!=correct:
		if guess>correct:
			print("Too high\n")
		elif guess<correct:
			print("Too low\n")
		guess = int(input())
	print("Your guess is right!!")

#high=int(input("Enter a max limit\n"))
#our_guess(high)

def computer_guess(high):
	ans=""
	low=0
	print("Enter c for correct h for high and l for low")
	guess = random.randint(low,high)
	while(ans!='c'):
		ans = input(f"{guess}?\n").lower()
		if ans=='h':
			high=guess-1
		elif ans=='l':
			low=guess+1
		guess = random.randint(low,high)
	print("Yaay!!! I answered it right!!!")

high=int(input("Enter a max limit\n"))
computer_guess(high)