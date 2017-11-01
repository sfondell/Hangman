import random

def hangman():
	lives = 5
	
	with open('words.txt') as f:
		lines = f.read().splitlines()
	key = lines[random.randint(0, len(lines))]
	key = str.lower(key)

	dist_letters = ''
	key_letters = 0
	for i in key:
		if i not in dist_letters:
			dist_letters += i
			key_letters += 1

	correct = ''
	guessed = ''
	while (True):
		if key_letters == 0:
			letter = str(raw_input('You won! play again? y or n: '))
			while len(letter) > 1 or letter not in 'yn':
				letter = str(raw_input('Please enter y or n: '))
			if letter == 'y':
				hangman()
			else:
				break
		else:
			if lives == 0:
				letter = str(raw_input('You are out of lives, play again? y or n: '))
				while len(letter) > 1 or letter not in 'yn':
					letter = str(raw_input('Please enter y or n: '))
				if letter == 'y':
					hangman()
				else:
					break
			else:
				letter = str(raw_input('Enter a guess: '))
				while (len(letter) > 1):
					letter = str(raw_input('Please enter only one letter: '))
				while (not str.isalpha(letter)):
					letter = str(raw_input('Please enter a letter guess: '))
				letter = str.lower(letter)
				if letter in guessed:
						print 'You already guessed ' + str(letter)
				elif letter in key:
					guessed += letter
					key_letters = key_letters - 1
					print letter + ' is in the word'
					correct += letter
					string = ''
					for i in key:
						if i.isspace():
							string += ' '
						elif i in correct:
							string += i
						else:
							string += '-'
					print string
				else:
					lives = lives - 1
					guessed += letter
					print letter + ' was not in the word, you have ' + str(lives) + ' lives left.'

hangman()


