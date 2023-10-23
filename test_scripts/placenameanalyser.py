file = open("test_scripts/placenames.txt","r")

names = []
for line in file:
    line = line.split("\t",1)
    if len(line) >= 2:
        del line[1]
    line = line[0]
    names.append(line)

file.close()

depth = int(input("Depth: "))
previousLetters = []
for i in range(depth):
    previousLetters.append("")


alphabet = ["START","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'","&","END"]
def define_weights(length,listDepth):
    if listDepth == 0:
        return 0
    else:
        theList = []
        for i in range(0,length,1):
            theList.append(define_weights(length,listDepth-1))
        return theList

weights = define_weights(len(alphabet) + 1,depth+1)

for name in names:
    name = name.lower()
    print(name)
    for letterIndex,letter in enumerate(name):
        for i in range(depth):
            previousLetterIndex = letterIndex - depth + i
            if previousLetterIndex > -1:
                previousLetter = name[previousLetterIndex].lower()
            else:
                previousLetter = "START"
            previousLetters[i] = previousLetter

        weights[alphabet.index(letter)][alphabet.index(previousLetters[-1])][alphabet.index(previousLetters[-2])] += 1

    weights[-2][alphabet.index(name[-1])][alphabet.index(name[-2])] += 1

totals = []
for penultimateLetterIndex in range(len(alphabet)):
    subTotals = []
    for lastLetterIndex in range(len(alphabet)):
        subTotal = 0
        for letterIndex in range(len(alphabet)):
            subTotal += weights[letterIndex][lastLetterIndex][penultimateLetterIndex]
        subTotals.append(subTotal)
    totals.append(subTotals)

weights[-1] = totals
print(weights)

file = open("town_name_weights.py","w")
file.write("weights = " + str(weights))
file.close