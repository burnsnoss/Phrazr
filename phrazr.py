import random
import sys

SCRUM_PHRAZEBOOK_PATH = './ScrumPhrazebook.txt'

def displayError(errorType):
	print 'ERROR'
	print 'CODE: 69'
	if errorType == 'runtime':
		print 'How to run Phrazr:'
		print '~$ python phrazr.py scrum'
		print '\nRight now, we only have one option, "scrum". Deal with it.'
		print 'run ~$ "python phrazr.py help" for more help.'
	elif errorType == 'arguments':
		print 'Please provide "scrum" as an argument.'
	return  

def printHelp():
	print '\nHow to run Phrazr:'
	print '~$ python phrazr.py scrum'
	print '"scrum" is currently the only option we support.'
	print '\nCopyright BonerJamz Inc. - Written by McFarts.' 
	return

def parseInput(argv):
	if len(argv) != 2:
		displayError('runtime')
		exit()
	else:
		if argv[1] == 'scrum':
			return 'scrum'
		elif argv[1] == 'help':
			printHelp()
			exit()
		else:
			displayError('arguments')
			exit()

def generatePhraze(cmd):
	if cmd == 'scrum':
		phraze = getScrumPhraze()
		print phraze
		exit()
	else:
		displayError('runtime')

def getScrumPhraze():
	filestream = open(SCRUM_PHRAZEBOOK_PATH, 'r')
	phrazes = filestream.read().split('\n')
	idx = random.randint(0, len(phrazes))
	return phrazes[idx]

if __name__ == '__main__':
	cmd = parseInput(sys.argv)
	generatePhraze(cmd)
	exit()
