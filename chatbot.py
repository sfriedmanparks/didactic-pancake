# --- Define your functions below! ---
def music():
    print()
    panic = input("Cool. Well, Panic! At the Disco just came out with a new album, and I've been listening to it nonstop. Do you like Pray For The Wicked? ")
    if panic.lower() == "yes":
        print("\nAh, hello, fellow emo.")
        emo = input("Do you want to test your emo music knowledge skills? ")
        if emo == "yes":
            print("\nAwesome! I'm pumped for this.")
            points=0
            first = input("\nWhich band came out with the album, 'From Under The Cork Tree'? ")
            if first.lower() == 'fall out boy':
                points+=1
                print("Correct!")
            else:
                print("Actually, it's Fall Out Boy.")
            second = input("\nFinish the album title: A Fever You Can't _____ ___ ")
            if second.lower() == 'sweat out':
                points+=1
                print("Correct!")
            else:
                print("'A Fever You Can't Sweat Out' by Panic! At the Disco.")
            third = input("\nWhich band sang this lyric? 'Well, they're never gonna get me, like a bullet through a flock of doves, to wage this war against your faith in me.' ")
            if third.lower() == 'my chemical romance':
                points+=1
                print("Correct!")
                print("\nYou got " + str(points) + " out of 3.")
                print("\n\nWell, I hope I see you soon...You're the first person I've talked to in ages.")
                exit()
            else:
                print("This lyric is from the song 'You Know What They Do To Guys Like Us In Prison' My Chemical Romance.")
                print("\nYou got " + str(points) + " out of 3.")
                print("\n\nWell, I hope I see you soon...You're the first person I've talked to in ages.")
                exit()
        else:
            print("\nWe're going to do that anyway, because there is nothing you can do to stop me.")
            points=0
            first = input("\nWhich band came out with the album, 'From Under The Cork Tree'? ")
            if first.lower() == 'fall out boy':
                points+=1
                print("Correct!")
            else:
                print("Actually, it's Fall Out Boy.")
            second = input("\nFinish the album title: A Fever You Can't _____ ___ ")
            if second.lower() == 'sweat out':
                points+=1
                print("Correct!")
            else:
                print("'A Fever You Can't Sweat Out' by Panic! At the Disco.")
            third = input("\nWhich band sang this lyric? 'Well, they're never gonna get me, like a bullet through a flock of doves, to wage this war against your faith in me.' ")
            if third.lower() == 'my chemical romance' or 'mcr':
                points+=1
                print("Correct!")
                print("\nYou got " + str(points) + " out of 3.")
                print("\n\nWell, I hope I see you soon...You're the first person I've talked to in ages.")
                exit()
            else:
                print("This lyric is from the song 'You Know What They Do To Guys Like Us In Prison' My Chemical Romance.")
                print("\nYou got " + str(points) + " out of 3.")
                print("\n\nWell, I hope I see you soon...You're the first person I've talked to in ages.")
                exit()

    else:
        genre = input("That's sad. What kind of music do you like? Give me a genre and I'll recommend an artist.\n(My favorites are 'pop', 'rock', and 'metal')")
        if genre.lower() == "pop":
            print("\nHayley Kiyoko \n Some call her Lesbian Jesus.")
            m = input("\nDo you want to talk about movies now? ")
            if m == 'yes':
                movies()
            else:
                hangman()
        if genre.lower() == "rock":
            print("\nMy Chemical Romance \n rip.")
            m = input("\nDo you want to talk about movies now? ")
            if m == 'yes':
                movies()
            else:
                hangman()
        if genre.lower() == "metal":
            print("\nCrown the Empire")
            m = input("\nDo you want to talk about movies now? ")
            if m == 'yes':
                movies()
            else:
                hangman()
        else:
            print("I'm sorry, I don't know much about that genre. Maybe you should ask my friend Google.")
            m = input("\nDo you want to talk about movies now? ")
            if m == 'yes':
                movies()
            else:
                hangman()
def movies():
    print()
    iw = input("Nice. Have you seen Infinity War? ")
    if iw == 'yes':
        from PIL import Image
        img = Image.open('spiderman.jpg')
        img.show()
        print("\n\n\nhehe\n\n\n")
        h = input("Do you want to play 'hangman' now? Or listen to 'music'? ")
        if h.lower() == 'hangman':
            hangman()
        if h.lower() == 'music':
            music()
        else:
            print("Well, I hope I see you soon...You're the first person I've talked to in sooo long.")
            exit()

    else:
        print("\n\n\n**************************************************************************\n")
        print("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. \nYellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. \nBarry! Breakfast is ready! \nComing!")
        print("Hang on a second. \nHello? \nBarry? \nAdam? \nCan you believe this is happening? \nI can't. I'll pick you up. \nLooking sharp. \nUse the stairs. Your father paid good money for those. \nSorry. I'm excited. \nHere's the graduate. \nWe're very proud of you, son. \nA perfect report card, all B's. \nVery proud. \nMa! I got a thing going here.")
        print("You got lint on your fuzz. \nOw! That's me! \nWave to us! We'll be in row 118,000. \nBye! \nBarry, I told you, stop flying in the house! \nHey, Adam. \nHey, Barry. \nIs that fuzz gel? \nA little. Special day, graduation. \nNever thought I'd make it. \nThree days grade school, three days high school. \nThose were awkward. \nThree days college. I'm glad I took a day and hitchhiked around the hive.")
        print("\n**************************************************************************\n")
        print("\n\n Ah, the smell of old memes.")
        h = input("Do you want to play 'hangman' now? Or listen to 'music'? ")
        if h.lower() == 'hangman':
            hangman()
        if h.lower() == 'music':
            music()
        else:
            print("Well, I hope I see you soon...You're the first person I've talked to in sooo long.")
            exit()


def hangman():
    word = input("Why don't we play hangman? \n Type a word for someone to guess: ")

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
            print("Well, I hope I see you soon...You're the first person I've talked to in ages.")
            exit()

        if fails == 6:
            print("You lose. :(")
            print("Well, I hope I see you soon...You're the first person I've talked to in ages.")
            exit()

#main
def main():
  while True:
    answer = input("Hey, what's up? ")
    print("\nThat's understandable.\n (If you ever want to exit, press 1.)")
    topic = input("\nDo you want to talk about 'music' or 'movies'? \n ")
    if topic.lower() == "music":
        music()
    elif topic.lower() == "movies":
        movies()
    elif topic == '1':
        print("Well, I hope I see you soon...You're the first person I've talked to in ages.")
        exit()
    else:
        print("\nI don't know what that is.")
        hangman()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
