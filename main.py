#select a random word 
#give number of letters as a clue
#can only guess one letter at a time until word guessed correctly or 6 incorrect tries
#player cannot guess same letter twice; program will notify player and let player guess again 
#if guess letter correctly, program replaces _ with the correct letter. 

import random 

wordList = []
with open("wordList.txt") as file:
	for line in file:
		wordList.append(line.strip())

gameword = random.choice(wordList)

print("Guess the word!")
for x in range(len(gameword)):
	print("_", end="")
print()

playing = []
for x in range(len(gameword)):
	playing.append("_")

lettersguessed = []

wrongguess = 0
while wrongguess < 6:
	letter = input("Guess a letter!: ")
	for x in range(len(lettersguessed)):
		if lettersguessed[x] == letter:
			print("You already guessed this! Try again!")
	for x in range(len(gameword)):
		if gameword[x] == letter:
			playing[x] = letter
			lettersguessed.append(letter)
	print(playing)
	if letter not in gameword:
		wrongguess += 1
		lettersguessed.append(letter)
		print("That was incorrect!")
		print(playing)

	if '_' not in playing:
		print("You guessed the word!")
		break


if wrongguess == 6:
	print("You lose!")
print("The word was: ", gameword)
