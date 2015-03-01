# Start of stage 4
#open text file
r = open("stage3_ciphertext", "r")
ciphertext = r.read()
#frequency of letters
genFreq = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]

def cleaner(string):
    cleantext = ""
    for i in string:
        if i != "*":
            cleantext += i
    #print(cleantext)
    return(cleantext)
        
def build(string):
    Built = []
    for x in range(0, (len(string)), 2):
        count = 0
        y = string[x:x+2]
        #print(y)
        Built.append(y)
    #print(Built)
    return(Built)

def freq(alphabet, string):
    print(alphabet)
    specFreq = [[0 for j in range(2)] for i in range(len(alphabet))]
    #print(specFreq)
    position = 0
    for symbol in alphabet:
        count = 0
        #print(symbol)
        for x in range(0, len(string), 2):
            #print(x)
            if symbol == string[x:x+2]:
                count = count+1
        specFreq[position] = (symbol, count)
        position = position+1
    return(specFreq)

Clean = cleaner(ciphertext)
SymbolList = build(Clean)
#print(SymbolList)
print(freq(SymbolList, Clean))

def getKey(item):
    
    return item[1]