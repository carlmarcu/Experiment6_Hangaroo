def getGuessedWord(secretWord, lettersGuessed):
    temp=[]
    w = ""
    for i in secretWord:
        if i in lettersGuessed:
            w += i
        else:
            w += "_ "
    return w
        
            