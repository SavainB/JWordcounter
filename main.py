f = open("note.txt", "r")
number_of_word = 0
words = []
summary = []
nomber = []
word = ""
for x in f:
    for e in x:
        if (e.isalpha()):
            word +=e
        else:
            words.append(word)
            word=""
nb = 0
def verify(mot):
    for i in summary:
        if (x == i):
            return False
    return True
for x in words:
    if (verify(x) and x != ""):
        if (x !=''):
            number_of_word +=1
        for i in words:
            if (x == i):
                nb += 1
        summary.append(x)
        nomber.append(nb)
        nb = 0

for (i,e) in zip(summary,nomber):   
    print(i,e)    
        
        