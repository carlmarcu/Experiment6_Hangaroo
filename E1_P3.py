def getAvailableLetters(lettersGuessed):
    w = ""
    c= 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for l in alphabet:
        if l in lettersGuessed:
            c+=1
        else:
            w+=l
    return w