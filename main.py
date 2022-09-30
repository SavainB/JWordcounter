from ast import Try
import PyPDF2
import sys


def verify(word, summary):
    for i in summary:
        if word == i:
            return False
    return True


def how_much_word(f):
    words = []  # list of word with space
    summary = []  # list of word wihout space and duplicate
    nomber = []  # will contain the how much word are in document
    word = ""
    number_of_word = 0
    nb = 0  # nomber of time the word is
    for x in f:
        for character in x:
            if character.isalpha():
                word += character
            else:
                words.append(word)
                word = ""
    for word in words:
        if verify(word, summary) and word != "":
            for i in words:
                if word == i:
                    nb += 1
            summary.append(word)
            nomber.append(nb)
            nb = 0
    for (word, number_of_time) in zip(summary, nomber):
        number_of_word += number_of_time
        print("[", word, "] =", number_of_time)
    print("Il y à ", number_of_word, "de mot dans le document.")


try:
    with open(sys.argv[1], 'r') as my_file:
        if my_file.name.endswith('.txt'):
            text_file = open(my_file.name, "r")
            how_much_word(text_file)
        elif my_file.name.endswith('.pdf'):
            pdf_file = open(my_file.name, "rb")
            # creating a pdf reader object
            fileReader = PyPDF2.PdfFileReader(pdf_file)
            page = fileReader.pages[0]
            # print the number of pages in pdf file
            # print(page.extract_text())
            pdf_file = page.extract_text()
            how_much_word(pdf_file)
        else:
            print("On accepte que les fichiers .TxT ou .PDF")
except:
    print("Auncun fichier \n Oubliez pas de lancer le fichier avec un .pdf ou txt")
