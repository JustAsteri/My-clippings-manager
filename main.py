import re

clippings_route = '/home/justasteri/1_PROJECTS/My-clippings_manager/cp.txt'
delimitator = '=========='
bookTitles = list()

try:
    clippings = open(clippings_route, "r+")
except:
    print("Error opening the file")

text = clippings.read()
nHght = text.count(delimitator)

nDelI = 0
nDelF = 0
for i in range(nHght):
    # === Loop to obtain each hl ====.
    nDelF = nDelI + 10 + text.find(delimitator)
    hl = text[:nDelF]
    print("nDelI = " + str(nDelI) + "\nnDelF = " + str(nDelF) + "\n\n")
    print(text[191:785])
    # print(text[nDelI:nDelF])
    # print(hl)
    nDelI = nDelF
    text = text[nDelI:]

    print("++++++++++++++++++++++++++++++++++++++++++++++")

    bookTitle = hl[:hl.find(")")]
    # print("TITULO: " + bookTitle)
    # if bookTitle not in bookTitles:
    #     bookTitles.append(bookTitle)
    # text = text[nDelF+10:]

# print(bookTitles)

counter = 0
#for i in bookTitles:
#    print("Choose the book to delete their hightlights: \n")
#    print(str(counter) + ". " + bookTitle)

clippings.close()