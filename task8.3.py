import random

listOfWords = ['APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE', 'ENSURING', 'FORMALISING', 'GLITCHES', 'HARMINE',
               'INDENTATION', 'JACKED', 'KALPACS',
               'LAUNDRY', 'MASKED', 'NETTED', 'OXFORD', 'PARODY', 'QUOTIENTS', 'RACERS', 'SADNESS', 'THYREOID', 'UNDUE',
               'VENT', 'WEDGED', 'XERIC', 'YOUTHHOOD', 'ZIFFS']
a = listOfWords[random.randint(0, len(listOfWords)-1)]
#print(a)
l = []
w = []
g = []
i = 0
while i < len(a):
    l.append('-')
    w.append(a[i])
    i = i + 1
print(l)
#print(w)
incor = 0
print("You have 6 Choices.")
z = True
while z and incor < 6:
    n = str(input("Guess your letter: ").upper())
    x = 0
    flag = False
    if (n in g):
        print("Already entered!")
    else:
        for i in w:
            if n.upper() == i:
                l[x] = n.upper()
                flag = True
                g.append(n.upper())
            x = x + 1

        if (flag == False):
            incor = incor +1
            print("inCorrect!")
            print(str(6 - incor) + " choices left")
        else:
            print(l)
        if (l == w):
            z = False


if z == False:
    print("You win!")
if incor == 6:
    print("You Lose!")
