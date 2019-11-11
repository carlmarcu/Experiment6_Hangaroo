def Hangaroo(secretWord):
    l=len(secretWord)
    print("IT'S HANGAROO TIME!")
    print("The word is", l, "letters long.")
    c=4
    i=0
    lettersGuessed=[]
    while (c!=0):
        if secretWord!= getGuessedWord(secretWord,lettersGuessed):
            print(c, "Chances left.")
            print("Available letters: ", getAvailableLetters(lettersGuessed))
            g=input("Go and type a letter: ")
            guessInLowerCase = g.lower()
            
            if guessInLowerCase in lettersGuessed:
                print("Oops, letter is already there: ", getGuessedWord (secretWord, lettersGuessed))
                
            elif guessInLowerCase not in secretWord:
                print("Snap, the letter is not in the word: ", getGuessedWord (secretWord, lettersGuessed))
                c-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Great!:",getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            print ("Congratulations! *WOOT* *WOOT*")
            break
        
    else:
        print("Aaww Sad. There are no more chances left. The word is " + secretWord)