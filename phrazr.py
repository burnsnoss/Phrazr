import random
import sys

SCRUM_PHRAZEBOOK_PATH = './ScrumPhrazebook.txt'
CASEY_PHRAZEBOOK_PATH = './CaseyPhrazebook.txt'
TY_PHRAZEBOOK_PATH = './TyPhrazebook.txt'

options = ['-casey', '-scrum', '-ty']

def displayError(errorType):
	print 'ERROR'
	print 'CODE: 69'
	if errorType == 'runtime':
		print 'How to run Phrazr:'
		print '~$ python phrazr.py -option'
		print '\nRight now, we only have two options, "-scrum" and "-casey". Deal with it.'
		print 'run ~$ "python phrazr.py -help" for more help.'
	elif errorType == 'arguments':
		print 'Please provide "-scrum" or "-casey" as an argument.'
	return  

def printHelp():
	print '\nHow to run Phrazr:'
	print '~$ python phrazr.py -option'
	print '"-scrum" and "-casey" are currently the only options we support.'
	print '\nCopyright BonerJamz Inc. 2017 - Written by McFarts.' 
	return

def parseInput(argv):
	if len(argv) != 2:
		displayError('runtime')
		exit()
	else:
		if argv[1] in  options:
			return argv[1]
		elif argv[1] == '-help':
			printHelp()
			exit()
		else:
			displayError('arguments')
			exit()

def generatePhraze(cmd):
	if cmd == '-scrum':
		phraze = getPhraze(SCRUM_PHRAZEBOOK_PATH)
	elif cmd == '-casey':
		phraze = getPhraze(CASEY_PHRAZEBOOK_PATH)
	elif cmd == '-ty':
		phraze = getPhraze(TY_PHRAZEBOOK_PATH)
	else:
		displayError('runtime')
		exit()
	print phraze
	return

def getPhraze(phrazebook):
	filestream = open(phrazebook, 'r')
	phrazes = filestream.read().strip('\n').split('\n')
	idx = random.randint(0, len(phrazes) - 1)
	print 'Index: ', idx
	print '#Phrazes: ', len(phrazes)
	return phrazes[idx]

if __name__ == '__main__':
	cmd = parseInput(sys.argv)
	generatePhraze(cmd)
	exit()
