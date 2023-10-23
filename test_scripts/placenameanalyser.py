file = open("placenames.txt","r")

names = []
for line in file:
    line = line.split("\t",1)
    if len(line) >= 2:
        del line[1]
    line = line[0]
    names.append(line)

file.close


depth = int(input("Depth: "))


alphabet = ["START","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-","'","&","END"]
weights = []
for i in range(0,len(alphabet)):
    weights.append([0 for i in range(len(alphabet))])

for name in names:
    for letterIndex,letter in enumerate(name):
        lastLetterIndex = letterIndex - 1
        lastLetter = name[lastLetterIndex]
        penultimateLetterIndex = letterIndex - 2
        penultimateLetter = name[penultimateLetterIndex]
        if lastLetterIndex <= -1:
            lastLetterIndex = -1
        if penultimateLetterIndex <= -1:
            penultimateLetterIndex = -1

totals = []
for letterWeight in range(0,len(alphabet),1):
    total = 0
    for letter in range(0,len(alphabet),1):
        total += weights[letter][letterWeight]
    totals.append(total)
weights.append(totals)