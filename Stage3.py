# Start of stage 3
import collections
#open text file
r = open("stage3_ciphertext", "r")
ciphertext = r.read()
#frequency of letters
genFreq = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]

def cleaner(string, needle):
    cleantext = ""
    for i in string:
        if i != needle:
            cleantext += i
    #print(cleantext)
    return(cleantext)
        
def build(string, num):
    # grab characters, "num" at a time 
    Built = []
    for x in range(0, (len(string)), num):
        count = 0
        y = string[x:x+num]
        #print(y)
        Built.append(y)
    #print(Built)
    return(Built)

def freq(alphabet, string, num):
    #print(len(alphabet))
    specFreq = [[0 for j in range(num)] for i in range(len(alphabet))]
    #print(specFreq)
    position = 0
    for symbol in alphabet:
        count = 0
        #print(symbol)
        for x in range(0, len(string), num):
            #print(x)
            if symbol == string[x:x+num]:
                count = count+1
        specFreq[position] = (symbol, count)
        position = position+1
    return(specFreq)

def getKey(item):
    
    return item[1]

def get0Key(item):
    return item[0]

def dedupe(Symbols):
    output = []
    seen = set()
    for Symbol in Symbols:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if Symbol not in seen:
            output.append(Symbol)
            seen.add(Symbol)
    return output

def FreqAnalysisCounter(array):
    counts=[x[1] for x in array]
    #print (counts)
    counter=collections.Counter(counts)
    return counter

# Start of program
alphabetCharLength=2
charToClean=""

Clean = cleaner(ciphertext, charToClean)

SymbolList = build(Clean, alphabetCharLength)
print(SymbolList)

DedupedSymbolList = dedupe(SymbolList)
print(DedupedSymbolList)

FreqCipherText = freq(DedupedSymbolList, Clean, alphabetCharLength)

Ordered = sorted(FreqCipherText, key = getKey, reverse = True)
print(Ordered)
print "Number of alphabet symbols:", (len(Ordered))
print "Frequency distribution", FreqAnalysisCounter(Ordered)
        