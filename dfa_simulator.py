# Hung Nguyen CSCE 355
# Choice 1: DFA Simulation
import sys
import re
from collections import OrderedDict
dfa_description = []
dfa = OrderedDict()
F = []

def dfaDescription():
	global F
	dfa_description = [line.rstrip('\n') for line in open(sys.argv[1])]
	# Getting # of States, Putting Accepting States and Alphabet into it's own LIST.
	Q = int(''.join(x for x in dfa_description[0] if x.isdigit()))
	F = [int(x) for x in dfa_description[1].split() if x.isdigit()]
	E = [x for x in dfa_description[2][10:]]
	#Putting in dict
	for i in range(Q):
		dfa[i] = OrderedDict()
		for x in E:
			dfa[i][x] = ''
	# Messing and converting for ease of access/traverse
	transition_table = [x for x in dfa_description[3:]]
	for i in range(len(transition_table)):
		transition_table[i] = re.findall('\d+', transition_table[i])
	#Matching inputed transition to dict
	for states in dfa:
		for idx, x in enumerate(dfa[states]):
			for y in range(len(E)):
					dfa[states][x] = transition_table[states][idx]
# Function to check if string is accepted or not
def output():
	try:
		strings = [line.rstrip('\n') for line in open(sys.argv[2])]
	except Exception as error:
		print("You did not provide a second file as argument!", error)
	## Looping through all input strings and checking against the dictionary
	try:
		# Looping through the dfa with given string starting at '0' as start
		for x in strings:
			S = '0'
			for e in x:
				# print("Current State: ", S, "char: ", e, end='')
				S = dfa[int(S)][e]
				# print(" New State: ", S)
			if int(S) in F:
				print("accept")
			else:
				print("reject")
	except Exception as error:
		print("Please check the input string again to make sure it matches! Error thrown at char: ", error)

dfaDescription()
output()
