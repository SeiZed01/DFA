#Hung Nguyen CSCE 355
# Inverse Homorphism

import sys
import re
from collections import OrderedDict

def findInverse():

    dfa = OrderedDict()
    dfa_description = [line.rstrip('\n') for line in open(sys.argv[1])]
    #Getting # of States, Final States, and Alphabet
    Q = int(''.join(x for x in dfa_description[0] if x.isdigit()))
    F = [int(x) for x in dfa_description[1].split() if x.isdigit()]
    E = [x for x in dfa_description[2][10:]] # Output
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

    homo_description = [line.rstrip('\n') for line in open(sys.argv[2])]
    input_E = [x for x in homo_description[0][16:]]
    #Creating separate table for invhom
    homo_table = OrderedDict()
    for i in range(Q):
        homo_table[i] = OrderedDict()
        for x in input_E:
            homo_table[i][x] = ''
    # Saving h(w).. to run through given DFA and get states to assign
    h_strings = [x for x in homo_description[2:]]

    # Traversing through h(0), h(1), .... h(n) inside the DFA to match the state to the new homo table
    for idx, x in enumerate(input_E):
        for i in range(Q):
            S = i
            for y in h_strings[idx]:
                S = dfa[int(S)][y] # Traversing through DFA
            homo_table[i][x] = S # Found state so setting in new homo table

    print("Number of states:", Q)
    print(dfa_description[1])
    print("Alphabet: ",end="")
    for x in input_E:
        print(x,end="")
    print()
    for x in homo_table:
        for y in homo_table[x]:
            print(homo_table[x][y], end= " ")
        print()



findInverse()
