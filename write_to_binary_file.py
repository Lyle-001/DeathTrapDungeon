from town_name_weights import weights

file = open("town_name_weights.bin","w")


for letterIndex,letter in enumerate(weights):
	for lastLetterIndex,lastLetter in enumerate(letter):
		for penultimateLetterIndex,penultimateLetter in enumerate(lastLetter):
			binaryNumber = ((bin(weights[letterIndex][lastLetterIndex][penultimateLetterIndex])).strip("0b")).zfill(10)
			file.write(binaryNumber)


file.close()