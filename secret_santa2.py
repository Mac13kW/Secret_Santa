import random

"""
This is an improved (2.0) version of the secret santa script.
Shorter and faster.

Maciej Workiewicz 2016
"""

A = (["name1", "name2", "name3", "name4"])

random.shuffle(A)
B = []
B.append(A[len(A)-1])
for x in range(len(A)-1):
    B.append(A[x])

print("Assignment of secret santas --> (to) recipients")

for y in range(len(A)):
    print(str(A[y]) + " ---> " + str(B[y]))

