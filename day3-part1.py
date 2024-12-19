import re

def digiMule(input, wort):
    mus = r"mul\(\d{1,3},(\d{1,3})\)"
    such = re.findall(mus, input)
    if such:
        return such#.group()
    return None

input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

print(digiMule(input, "mul"))
multi = digiMule(input, "mul")
summe = 1
for i in multi:
    (a,b) = map(int,i)
    summe += a*b
        
    




print(summe)


    
