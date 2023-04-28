class Cp:
    cname: ""
    pdict = {}


# a=Cp()
a = 'sanidhya sahu'
# a.pdict.__setitem__("uc001",100)
b = []
# print(a.cname,a.pdict)
with open('materialcode.txt', 'r') as r:
    f = r.read()
    for word in f.splitlines():
        # i=str(i)
        j = Cp()
        j.cname = f'{word.split()}'
        print(j.cname)
        b.append(j.cname)

print(b[0])

