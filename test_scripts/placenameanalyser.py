file = open("test_scripts/placenames_sanitised.txt","r")
#sanitisedfile = open("test_scripts/placenames_sanitised.txt","w")

names = []
for line in file:
    line = line.split("\n")
    line = line[0]
    line = line.split("\t")
    line = line[0]
    line = line.split(",")
    line = line[0]
    

    if len(line) != 1:
        #sanitisedfile.write(line + "\n")
        names.append(line.lower())

file.close()

depth = int(input("Depth: "))
previousLetters = ""


alphabet = ["S","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'",".","&","E"]
def define_weights(length,listDepth):
    if listDepth == 0:
        return 0
    else:
        theList = []
        for i in range(0,length,1):
            theList.append(define_weights(length,listDepth-1))
        return theList
    
def define_weights_dictionary(dictionaryDepth):
    dictionary = {}
    if dictionaryDepth > 1:
        for letter in alphabet:
            dictionary[letter] = define_weights_dictionary(dictionaryDepth-1)
        dictionary["TOTAL"] = define_weights_dictionary(dictionaryDepth-1)
    return dictionary

weights = define_weights_dictionary(2)

for name in names:
    for letterIndex,letter in enumerate(name):
        if not letter in alphabet:
            print(letter + " was not found in the alphabet.")
            print("in name: " + name)
            input()
        previousLetters = ""
        for i in range(depth):
            previousLetterIndex = letterIndex - depth + i
            if previousLetterIndex > -1:
                previousLetter = name[previousLetterIndex].lower()
            else:
                previousLetter = "S"
            previousLetters += previousLetter
        if previousLetters in weights[letter]:
            weights[letter][previousLetters] += 1
        else:
            weights[letter][previousLetters] = 1
        if previousLetters in weights["TOTAL"]:
            weights["TOTAL"][previousLetters] += 1
        else:
            weights["TOTAL"][previousLetters] = 1
    if name[-depth:] in weights["E"]:
        weights["E"][name[-depth:]] += 1
    else:
        weights["E"][name[-depth:]] = 1
    if name[-depth:] in weights["TOTAL"]:
        weights["TOTAL"][name[-depth:]] += 1
    else:
        weights["TOTAL"][name[-depth:]] = 1

            

# for name in names:
#     name = name.lower()
#     print(name)
#     for letterIndex,letter in enumerate(name):
#         for i in range(depth):
#             previousLetterIndex = letterIndex - depth + i
#             if previousLetterIndex > -1:
#                 previousLetter = name[previousLetterIndex].lower()
#             else:
#                 previousLetter = "START"
#             previousLetters[i] = previousLetter

#         weights[alphabet.index(letter)][alphabet.index(previousLetters[-1])][alphabet.index(previousLetters[-2])] += 1

#     weights[-2][alphabet.index(name[-1])][alphabet.index(name[-2])] += 1

# totals = []
# for penultimateLetterIndex in range(len(alphabet)):
#     subTotals = []
#     for lastLetterIndex in range(len(alphabet)):
#         subTotal = 0
#         for letterIndex in range(len(alphabet)):
#             subTotal += weights[letterIndex][lastLetterIndex][penultimateLetterIndex]
#         subTotals.append(subTotal)
#     totals.append(subTotals)

# weights[-1] = totals
# print(weights)

file = open("town_name_weights_dictionary.py","w")
file.write("weights = " + str(weights))
file.close