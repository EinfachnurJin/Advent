input = """3   4
4   3
2   5
1   3
3   9
3   3"""


liste1 = []
liste2 = []

for zeile in input.splitlines():
    zahlen = zeile.split()
    liste1.append(int(zahlen[0]))
    liste2.append(int(zahlen[1]))

liste1.sort()
liste2.sort()
# print(liste1, liste2)

result = []

for (a,b) in zip(liste1, liste2):
    diff = a-b
    if diff < 0:
        diff = -diff
    result.append(diff)
    print(a,b, result)

res = sum(result)
print(res)