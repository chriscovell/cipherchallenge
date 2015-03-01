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
    #print(len(alphabet))
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

def getKey(item):
    
    return item[1]
def get0Key(item):
    return item[0]

def dedupe(Symbols):
    
    OrderedSymbols = sorted(Symbols, key = get0Key, reverse = True)
    print(OrderedSymbols)
    #print(len(OrderedSymbols))
    i = 0
    length = len(OrderedSymbols)
    while i < length-1:
        #print(len(OrderedSymbols))
        #print(i)
        if OrderedSymbols[i] == OrderedSymbols[i+1]:
            #print("Popping", OrderedSymbols[i])
            OrderedSymbols.pop(i)
            length = length-1
        i = i+1
    return(OrderedSymbols)

Clean = cleaner(ciphertext)
SymbolList = build(Clean)
#print(SymbolList)
OrderedSymbolList = dedupe(SymbolList)
print(OrderedSymbolList)
FreqCipherText = freq(OrderedSymbolList, Clean)

Ordered = sorted(FreqCipherText, key = getKey, reverse = True)
print(Ordered)