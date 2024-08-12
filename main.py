from random import choice

RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;93m"
ORANGE = "\033[1;38;5;166m"
WHITE = "\033[1;37m"
EOC = "\033[0m"

colors = ["R", "G", "B", "Y", "O", "W"]

lives = 10

def secret_combination(colors):
	secret_list = []
	for i in range(4):
		secret_list.append(choice(colors))
	
	return secret_list

def check_user_input(guess):
	if len(guess) != 4:
		return False
	
	for i in range(4):
		if len(guess[i]) != 1 or not guess[i].isalpha() or guess[i] not in colors:
			return False

	return True

def check_combination(secret, guess):
	color_counts = {}
	correct = 0
	incorrect = 0

	for color in secret:
		if color not in color_counts:
			color_counts[color] = 0
		color_counts[color] += 1
	
	for secret_color, guess_color in zip(secret, guess):
		if secret_color == guess_color:
			correct += 1
			color_counts[guess_color] -= 1
		
	for secret_color, guess_color in zip(secret, guess):
	        if guess_color != secret_color and guess_color in color_counts and color_counts[guess_color] > 0:
		        incorrect += 1
		        color_counts[guess_color] -= 1

	return correct, incorrect

def print_colors(colors):
	colored = ''
	for x in colors:
		colored += ''.join(' ')
		if x == "R":
			colored += ''.join(f"{RED}R{EOC}")
		elif x == "G":
			colored += ''.join(f"{GREEN}G{EOC}")
		elif x == "B":
			colored += ''.join(f"{BLUE}B{EOC}")
		elif x == "Y":
			colored += ''.join(f"{YELLOW}Y{EOC}")
		elif x == "O":
			colored += ''.join(f"{ORANGE}O{EOC}")
		elif x == "W":
			colored += ''.join(f"{WHITE}W{EOC}")

	return colored

secret = secret_combination(colors)

print(f"{WHITE}Welcome to mastermind you have {BLUE}10{WHITE} tries to guess the combinations...{EOC}")
print(f"{WHITE}The valid colors are:{EOC}{print_colors(colors)}\n")

tries = 0

while True:
	user_input = input(f"{BLUE}Guess{WHITE}:{EOC} ")
	guess = [x.upper() for x in list(user_input) if x != ' ']
	if not check_user_input(guess):
		print(f"{RED}Wrong format.{EOC}")
		continue
	else:
		tries += 1
		if guess == secret:
			if tries == 1:
				print(f"\n{WHITE}You guessed the combination in {BLUE}{tries}{WHITE} try !{EOC}")
			else:
				print(f"\n{WHITE}You guessed the combination in {BLUE}{tries}{WHITE} tries !{EOC}")
			print(f"{WHITE}The combination was{print_colors(secret)}.{EOC}")
			break
		else:
			correct,incorrect = check_combination(secret, guess)
			print(f"{BLUE}Correct positions{WHITE}: {GREEN}{correct}{WHITE} | {BLUE}Incorrect positions{WHITE}: {RED}{incorrect}{EOC}")
			lives -= 1
			if lives > 1:
				print(f"{WHITE}You have {RED}{lives}{WHITE} tries left.{EOC}\n")
			elif lives == 1:
				print(f"{WHITE}You have {RED}{lives}{WHITE} try left.{EOC}\n")
			else:
				print(f"\n{RED}You lose{WHITE}. The combination was{print_colors(secret)}.{EOC}")
				break
