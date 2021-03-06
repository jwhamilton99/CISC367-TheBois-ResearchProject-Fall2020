# main.py
# Author: Justin Hamilton
# This script reads a merged-pythondev-help-concat-group.csv" and removes emojis and acronyms (from a list of known acronyms "acro.txt").
# It uses regular expressions to find emojis (any length of non-whitespace characters between two colons) and the acronyms, then the re.sub() command to remove emojis and a string-concatenation algorithm to remove the acronyms. It also keeps track of the number of emojis and acronyms and a list of the text of each.
# An output CSV file, "output.csv", is generated containing the original message, the message with emojis and acronyms removed, the number of emojis and acronyms, and a list of the emojis and acronyms for each message.

import csv
import re

if __name__ == "__main__":
	chatsFile = open("merged-pythondev-help-concat-group.csv", "r")
	csvContent = csv.reader(chatsFile)
	
	acronyms = []
	
	acronymsFile = open("acro.txt", "r")
	acronymsContent = acronymsFile.read()
	for row in acronymsContent.split("\n"):
		acronyms.append(row)
	
	outFile = open("output.csv", "w")
	outFile.write("")
	outFile.write("messageText\tmessageTextPostProcessing\tnumEmojis\tnumAcronyms\temojis\tacronyms\n")
	
	outFile2 = open("output-excludedmessages.csv", "w")
	outFile2.write("")
	outFile2.write("messageText")
	
	i = 1
	emojiPattern = r':([\w]+[^ ]):'
	for row in csvContent:
		# to test, use the commented line and insert a max limit
		if(row.__len__() != 0 and i != 0):
		# if(row.__len__() != 0 and i != 0 and i < 200):
			message = re.sub("\n", " ", row[3])
			message = re.sub(r'`{3}(.+?)`{3}', "", message)
			numEmoji = 0
			numAcronyms = 0
			emojiList = []
			acronymList = []
			foundEmoji = False
			outputMessage = str(message)
			matchObj = re.search(emojiPattern, message)
			if(matchObj):
				outputMessage = (re.sub(emojiPattern, "", message))
				foundEmoji = True
				emojiList = re.findall(emojiPattern, message)
				numEmoji = emojiList.__len__()
			
			foundAcro = False
			for acro in acronyms:
				if(acro.__len__() < 2):
					continue
				pattern = (rf"(^|\s)({re.escape(acro)})($|\s)")
				match = re.search(pattern, outputMessage, re.IGNORECASE)
				
				if(match):
					acronymList.append(match.group(2))
					numAcronyms+=1
					foundAcro = True
					nOutput = outputMessage[:match.start()]
					nOutput+=" "
					nOutput+=outputMessage[match.end():]
					outputMessage = str(nOutput)
			
			if(foundAcro | foundEmoji):
				outFile.write(message+"\t"+outputMessage+"\t"+str(numEmoji)+"\t"+str(numAcronyms)+"\t"+str(emojiList)+"\t"+str(acronymList)+"\n")
			else:
				outFile2.write(message+"\n")
			
			i+=1
		
	chatsFile.close()
	outFile.close()
	outFile2.close()