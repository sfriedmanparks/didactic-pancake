word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")
else:
    blanks = []
    n=0
    while n < len(word):
        blanks.append("_")
        n += 1

    maxfails = 6
    fails = 0
    success = 0

    while fails < 6 and success < len(word):
        print(blanks)
        guess = input("Guess a letter: ")
        for i in range(0,len(word)):
            if guess == word[i]:
                blanks[i] = guess
                success += 1
        if(not(guess in word)):
            fails += 1
            print("No.")

    if success == len(word):
        print(blanks)
        print("You got it!")

    if fails == 6:
        print("You lose, try again! :(")
