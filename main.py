from ast import Try
import PyPDF2
import sys
def verify(word,summary):
    for i in summary:
        if word == i:
            return False
    return True
def how_much_word(f):
    words = []
    summary = []
    nomber = []
    word = ""
    number_of_word = 0
    nb = 0
    for x in f:
        for e in x:
            if e.isalpha():
                word += e
            else:
                words.append(word)
                word = ""
    for x in words:
        if verify(x,summary) and x != "":
                for i in words:
                    if x == i:
                        nb += 1
                summary.append(x)
                nomber.append(nb)
                nb = 0
    for (i, e) in zip(summary, nomber):
        number_of_word += e
        print("[",i,"] =", e)
    print("Il y à ",number_of_word,"de mot dans le document.")

try:
    with open(sys.argv[1], 'r') as my_file:
        if my_file.name.endswith('.txt'):
            file = open(my_file.name, "r")
            how_much_word(file)
        elif my_file.name.endswith('.pdf'):
            f = open(my_file.name, "rb")
            # creating a pdf reader object
            fileReader = PyPDF2.PdfFileReader(f)
            page = fileReader.pages[0]
            # print the number of pages in pdf file
            # print(page.extract_text())
            f = page.extract_text()
            how_much_word(f)
        else:
            print("On accepte que les fichiers .TxT ou .PDF")
except:
     print("Auncun fichier \n Oubliez pas de lancer le fichier avec un .pdf ou txt")
     


