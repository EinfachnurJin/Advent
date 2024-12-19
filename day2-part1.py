input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# && and

def isSafe(rep):
    fallend = True
    steigend = True

    for i in range(len(rep) - 1):
        diff = rep[i] - rep[i + 1]
        if  diff >=1 and diff <=3:
            steigend = False
        elif diff <= -1 and diff >= -3:
            fallend = False
        else:
             steigend = False
             fallend = False
        
    return fallend or steigend


reports = []
for i in input.splitlines():
    reports.append(list(map(int, i.split())))


anzahl = 0
for i in reports:
    if isSafe(i):
        anzahl = anzahl + 1
print(anzahl)

#print(reports)