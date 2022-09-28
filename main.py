import PyPDF2
import sys

with open(sys.argv[1], 'r') as my_file:
    if my_file.name.endswith('.txt'):
        print("txt")
        f = open(my_file.name, "r")
    elif my_file.name.endswith('.pdf'):
        print("pdf")
        f = open(my_file.name, "rb")
        # creating a pdf reader object
        fileReader = PyPDF2.PdfFileReader(f)
        page = fileReader.pages[0]
        # print the number of pages in pdf file
        # print(page.extract_text())
        f = page.extract_text()
    else:
        print("putain")


number_of_word = 0
words = []
summary = []
nomber = []
word = ""
for x in f:
    for e in x:
        if e.isalpha():
            word += e
        else:
            words.append(word)
            word = ""
nb = 0


def verify(mot):
    for i in summary:
        if x == i:
            return False
    return True

for x in words:
    if verify(x) and x != "":
        if x != "":
            number_of_word += 1
        for i in words:
            if x == i:
                nb += 1
        summary.append(x)
        nomber.append(nb)
        nb = 0
number_of_word = 0
for (i, e) in zip(summary, nomber):
    number_of_word += e
    print(i, e)
print(number_of_word)
