import re
def deleteLeadingZeros(inputString):
   for k in range(len(inputString)):
      if inputString[k] != '0':
         outputString= inputString[k::]
         return outputString
   return "0"
def printInput(innp):
    inp = innp
    inp = re.sub('\\D', '', inp)
    inp = deleteLeadingZeros(inp)
    inpint=int(inp)
    return inp,inpint