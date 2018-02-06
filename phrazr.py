import random
import sys

# TO DO: read these paths in by looking for files with regex *Phrazebook.txt
#  Then how to do options?

SCRUM_PHRAZEBOOK_PATH = './ScrumPhrazebook.txt'
CASEY_PHRAZEBOOK_PATH = './CaseyPhrazebook.txt'
TY_PHRAZEBOOK_PATH = './TyPhrazebook.txt'
TEAM_PHRAZEBOOK_PATH = './TeamPhrazebook.txt'
RANDOM_PHRAZEBOOK_PATH = './RandomPhrazebook.txt'
NATHANSDAD_PHRAZEBOOK_PATH = './NathansDadPhrazebook.txt'

options = {
	'-casey': CASEY_PHRAZEBOOK_PATH,
	'-scrum': SCRUM_PHRAZEBOOK_PATH,
	'-ty': TY_PHRAZEBOOK_PATH,
	'-team': TEAM_PHRAZEBOOK_PATH,
	'-random': RANDOM_PHRAZEBOOK_PATH,
	'-nathansdad': NATHANSDAD_PHRAZEBOOK_PATH
}

def displayError(errorType):
	print 'ERROR'
	print 'CODE: 69'
	if errorType == 'runtime':
		print 'Improper number of command line arguments. Shame on you.'
	elif errorType == 'arguments':
		print 'Invalid command line option.'
	elif errorType == 'agglength':
		print 'Invalid aggregate length.'
	printHelp()

	return  

def printHelp():
	print '\nHow to run Phrazr:'
	print '~$ python phrazr.py -option'
	print 'Currently, we support these options:'
	print ''
	for opt in options:
		print '\t', opt
	print '\nCopyright BonerJamz Inc. 2017 - Written by McFarts.' 
	return

def parseInput(argv):
	if len(argv) != 2:
		displayError('runtime')
		exit()
	else:
		if argv[1] in options.keys() or argv[1] == '-aggregate':
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

def generateAggregatePhraze(length):
	hashnum = 9437
	aggbook = []
	for opt in options:
		filestream = open(options[opt], 'r')
		phrazes = filestream.read().strip('\n').split('\n')
		for i in range(len(phrazes)):
			aggbook.append(phrazes[i].split(' '))
		phrazes = []
	
	phraze = ''
	for j in range(length):
		idx1 = ((random.randint(0, len(aggbook) - 1) + random.randint(0, 10000)) * hashnum) % len(aggbook)
		idx2 = ((random.randint(0, len(aggbook[idx1]) - 1) + random.randint(0, 10000)) * hashnum) % len(aggbook[idx1])
		phraze += aggbook[idx1][idx2] + ' '

	print phraze
		
		

if __name__ == '__main__':
	cmd = parseInput(sys.argv)
	if cmd == '-aggregate':
		phraze_length = raw_input('Length of phraze? [1-12] --> ')
		if phraze_length.isdigit() and int(phraze_length) > 0 and int(phraze_length) <= 12:
			generateAggregatePhraze(int(phraze_length))
		else:
			printError('agglength')
			exit()
	else:
		generatePhraze(cmd)
	exit()
