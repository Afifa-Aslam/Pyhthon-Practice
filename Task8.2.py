def hangman():
    word=['E','V','A','P','O','R','A','T','E']
    length=len(word)
    guess=[]
    for x in range(length):
        guess.append("-")
    a=1
    while a==1:
        i=input("Guess Your Letter :")
        if i in word:
            for x in range(length):
                if i==word[x]:
                    guess[x]=i
                    print(" ".join(guess))
                    if "-" not in guess:
                        print("You Win!")
                        a=2
        else:
            print("Incorrect")
print("Welcome to hangman")
hangman()
