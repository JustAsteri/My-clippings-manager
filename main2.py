import re

clippings_route = '/home/justasteri/1_PROJECTS/My-clippings_manager/cp.txt'
delimitator = '=========='
bookTitles = list()

try:
    clippings = open(clippings_route, "r+")
except:
    print("Error opening the file")

text = clippings.read()
n = 192 + 10 + (text[192:].find(delimitator))
print(text[192:n])
nHght = text.count(delimitator)

nDelI = 0
    #bookTitle = hglgt[:hglgt.find("\n")]
    #if bookTitle not in bookTitles:
    #    bookTitles.append(bookTitle)
    #text = text[nDelF+10:]
#print(bookTitles)

counter = 0
#for i in bookTitles:
#    print("Choose the book to delete their hightlights: \n")
#    print(str(counter) + ". " + bookTitle)

clippings.close()