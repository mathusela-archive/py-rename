import os
import sys

#install requirements
f = open("./firstRun.txt", "r+")
if f.read() == "True\n":
	os.system("pip3 install -r requirements.txt")
	f.write("REMOVE THIS TEXT LEAVING ONLY \"True \\n\" TO REINSTALL PACKAGES")

from termcolor import colored as col

def help():
	help = [	" ",
		col(	"		DOCUMENTATION/HELP PAGE:", "red"),
		col(	"		for full documentation refer to README.md", "cyan"),
			" ",
		col(	"		COMMON SYNTAX", "yellow"),
			"			all commands are executed through the syntax:",
			"			python3 pyRename.py ...",
			" ",
		col(	"		FLAGS", "yellow"),
			"			--help	display help		DISPLAYS THIS HELP PAGE",
			"			-rb	remove before		REMOVES EVERYTHING BEFORE SPECIFIED CHAR",
			"			-ra	remove after		REMOVES EVERYTHING AFTER SPECIFIED CHAR",
			"			-c	replace char		CHANGES EVERY INSTANCE OF A SPECIFIED CHAR",
			"			-n	numbered		CONVERTS ALL FILE NAMES INTO NUMBERED NAMES IN A SPECIFIED ORDER",
			"			-e	modify extention	MODIFIES FILE EXTENTION",
			" "]
	#print(help)
	for line in help:
		print(line)
	sys.exit(0)

def removeBefore():
	print(os.listdir(sys.argv[4]))
	newNameList = []
	for i in os.listdir(sys.argv[4]):
		newName = ""
		startName = False
		for char in i:
			if sys.argv[2] == "true" or sys.argv[2] == "True" or sys.argv[2] == "T" or sys.argv[2] == "t":
				if startName:
					newName += char
				if char == sys.argv[3]:
					startName = True
			else:
				if char == sys.argv[3]:
					startName = True
				if startName:
					newName += char
		newNameList.append(newName)
	return newNameList

if sys.argv[1] == "-rb":
	namesResult = removeBefore()
elif sys.argv[1] == "-ra":
	namesResult = removeAfter()
elif sys.argv[1] == "-c":
	namesResult = changeChar()
elif sys.argv[1] == "-n":
	namesResult = numbered()
elif sys.argv[1] == "-e":
	namesResult = extention()
elif sys.argv[1] == "--help":
	help()

print(namesResult)
