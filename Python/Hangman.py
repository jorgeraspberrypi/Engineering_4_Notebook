#Python Challenge - Hangman
#Written by Kaylee and Gabby

turns = 0

word = input("Player 1, what is the word")
print("\n" * 50)
print("i just need an array with " + str(len(word)) + " blanks in it.")

guess = input("Player 2, guess a letter")
guessniw = []
guessiw = []


    guessiw.append("_")

def printguy(t):
    if t < 1:
        print("---|")
    if t == 1:
        print("---|")
        print("   O")
    if t == 2:
        print("---|")
        print("   O")
        print("   |")
        print("   |")
    if t == 3:
        print("---|")
        print("   O")
        print("  /| ")
        print("   | ")
    if t == 4:
        print("---|")
        print("   O")
        print("  /|\ ")
        print("   | ")
    if t == 5:
        print("---|")
        print("   O")
        print("  /|\ ")
        print("   | ")
        print("  /  ")
    if t == 6:
        print("---|")
        print("   O")
        print("  /|\ ")
        print("   | ")
        print("  / \ ")
    if t == 7:
        print("---|")
        print("   O")
        print("  /|\ ")
        print("   | ")
        print(" _/ \ ")
    if t == 8:
        print("---|")
        print("   O")
        print("  /|\ ")
        print("   | ")
        print(" _/ \_")

    
while turns < 8:
    if guess not in word:
        turns += 1
        guessniw.append(guess)
    else:
        print("You got a letter")    
    printguy(turns)
    print(guessniw)
    print(guessiw)
    guess = input("Player 2, guess another letter")




for letter in word:
    for index,letter in enumerate(word):
        if letter == guess:
            guessiw[index] = guess
    guessiw.append(guess)        
