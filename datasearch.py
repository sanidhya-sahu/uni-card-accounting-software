with open('materialcode.txt', 'r') as document:
    mcodes = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        mcodes[line[0]] = line[1:]
mcodes.__setitem__('','')
mcodes.__setitem__(' ',' ')
mcodes.__setitem__('\n','\n')
# while (True):
# d=input()
# print(mcodes)
codem=dict()
for key in mcodes:
    val = mcodes[key]
    codem[str(val).replace('[', '', 100).replace("'", '', 100).replace(']', '', 100).replace('_', ' ', 100).upper()] = key
# print(codem)
def get_key(val):
    for key, value in mcodes.items():
        if val == value:
            return key
def datalookup(d):
    global a
    a=d
    key=a.upper()

    if key in mcodes.keys():
        co=1
        s = str(mcodes[a.upper()]).replace('[', '', 100).replace("'", '', 100).replace(']', '', 100).replace('_', ' ', 100)
        cs=s+f'  - ({key})'
        # print(cs)
        return cs,co
    else:
        co=2
        search_key=d.upper()
        res = dict(filter(lambda item: search_key in item[0], codem.items()))
        elem=str(res).replace('{','').replace('}','')
        print(elem)
        global sepc
        sepc=elem.split(',')
        print(sepc)
        sepel=str(sepc).split("'")
        return sepc



# datalookup(d)


