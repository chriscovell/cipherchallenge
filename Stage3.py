# Start of stage 3
import collections
#open text file
r = open("stage3_ciphertext", "r")
ciphertext = r.read()
#frequency of letters
#genFreq = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
# Italiano genFreq = ["e", "a", "i", "o", "n", "l", "r", "t", "s", "c", "d", "p", "u", "m", "v", "g", "z", "f", "b", "h", "q", "w", "y", "j", "k", "x"]
genFreq = ["i", "a", "r", "p", "n", "l", "e", "s", "t", "c", "d", "o", "u", "m", "v", "g", "z", "y", "b", "h", "q", "w", "f", "j", "k", "x"]

def decrypt(baseFreq, ourFreq, character):
    # find our character in ourFreq map
    
    if character == "G" or character == "C" or character == "B":
        return("i")
    if character == "M" or character == "Z" or character == "N":
        return("a")
    
    for c in range(0,26):
        tup=ourFreq[c]
        if tup[0]==character:
            return baseFreq[c]
    # return the appropriate character out of the baseFreq list
    return character

def Replacer(Replace, Replacee, Text):
    ReplacedText = ""
    for i in Text:
        if i == Replace:
            ReplacedText += Replacee
        else:
            ReplacedText += i
        
    return(ReplacedText)

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
alphabetCharLength = 1
charToClean = ""
CharToReplace = "X"
CharToReplaceWith = " "

Clean = cleaner(ciphertext, charToClean)

SymbolList = build(Clean, alphabetCharLength)
#print(SymbolList)

DedupedSymbolList = dedupe(SymbolList)
print(DedupedSymbolList)

FreqCipherText = freq(DedupedSymbolList, Clean, alphabetCharLength)

Ordered = sorted(FreqCipherText, key = getKey, reverse = True)
print(Ordered)
print ("Cipher text length is: ", len(ciphertext))
print ("Number of alphabet symbols:", (len(Ordered)))
print ("Frequency distribution", FreqAnalysisCounter(Ordered))
ReplacedCipherText = Replacer(CharToReplace, CharToReplaceWith, ciphertext)
print (ReplacedCipherText)
plainText=""
for character in ReplacedCipherText:
    # send each character in our cipher to the decrypt function
    newChar=decrypt(genFreq, DedupedSymbolList, character)
    # build up our plain text
    plainText += newChar

print(plainText)
        