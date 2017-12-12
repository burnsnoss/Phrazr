import random
import sys

SCRUM_PHRAZEBOOK_PATH = './ScrumPhrazebook.txt'
CASEY_PHRAZEBOOK_PATH = './CaseyPhrazebook.txt'
TY_PHRAZEBOOK_PATH = './TyPhrazebook.txt'
TEAM_PHRAZEBOOK_PATH = './TeamPhrazebook.txt'

options = {
	'-casey': CASEY_PHRAZEBOOK_PATH,
	'-scrum': SCRUM_PHRAZEBOOK_PATH,
	'-ty': TY_PHRAZEBOOK_PATH,
	'-team': TEAM_PHRAZEBOOK_PATH
}

def displayError(errorType):
	print 'ERROR'
	print 'CODE: 69'
	if errorType == 'runtime':
		print 'Improper number of command line arguments. Shame on you.'
	elif errorType == 'arguments':
		print 'Invalid command line option.'
	printHelp()

	return  

def printHelp():
	print '\nHow to run Phrazr:'
	print '~$ python phrazr.py -option'
	print 'Currently, we support these options:'
	print ''
	for opt in option:
		print '\t', opt
	print '\nCopyright BonerJamz Inc. 2017 - Written by McFarts.' 
	return

def parseInput(argv):
	if len(argv) != 2:
		displayError('runtime')
		exit()
	else:
		if argv[1] in options.keys():
			return argv[1]
		elif argv[1] == '-help':
			printHelp()
			exit()
		else:
			displayError('arguments')
			exit()

def generatePhraze(cmd):
	phraze = getPhraze(options[cmd])
	print phraze
	return

def getPhraze(phrazebook):
	filestream = open(phrazebook, 'r')
	phrazes = filestream.read().strip('\n').split('\n')
	idx = random.randint(0, len(phrazes) - 1)
	return phrazes[idx]

if __name__ == '__main__':
	cmd = parseInput(sys.argv)
	generatePhraze(cmd)
	exit()
