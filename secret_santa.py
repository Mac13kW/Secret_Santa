print '''
Secret Santa (ver 1.1)

Matches people for a Secret Santa party.
The script takes a list of names, creates a permutation of the first
list with no fixed point and prints out each match.

Maciej Workiewicz (2011-2014)
'''

# updated on December 12th, 2014 (ver 1.1)

from random import shuffle

names = (['name1', 'name2', 'name3'])
match = names[:]

x = 1
while x == 1:
    shuffle(match)
    for y in range(len(match)):
        if names[y] == match[y]:
            x = 1
            break
        else:
            x = 0
for z in range(len(match)):
    print names[z] + ' -- present --> ' + match[z]
