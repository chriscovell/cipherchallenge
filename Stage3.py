# Start of stage 3
import collections
#open text file
r = open("stage3_ciphertext", "r")
ciphertext = r.read()
#frequency of letters
#genFreq = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
# Italiano genFreq = ["e", "a", "i", "o", "n", "l", "r", "t", "s", "c", "d", "p", "u", "m", "v", "g", "z", "f", "b", "h", "q", "w", "y", "j", "k", "x"]

def decrypt(baseFreq, ourFreq, character):
    # find our character in ourFreq map
    
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
    numstring=len(string)
    
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
        percent=round(100.*count/numstring,2)        
        specFreq[position] = (symbol, count, percent)
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

def findDoubles(list, text):
    print("Doubles")
    for char in list:
        count=0
        prev=""
        for textbit in text:
            #print("char=", char, "textbit=", textbit, "prev=", prev, "count=",count)
            if((textbit==prev) and (textbit==char)):
                count=count+1
            prev=textbit   
        if(count>0):
            print(char,"-",count)
           
def findSingles(list, text):
    print("Singles")
    

    
# Start of program

alphabetCharLength = 1
charToClean = "X"
CharToReplace = ""
CharToReplaceWith = ""

# "G", "C" and "B" are homophones
# "M", "Z" and "N" are also homophones

# First, let's get our frequency statistics

#Clean = cleaner(ciphertext, charToClean)
#print(Clean)

#genFreq = [" ", "e", "a", "i", "o", "n", "l", "r", "t", "s", "c", "d", "p", "u", "m", "v", "g", "z", "f", "b", "h", "q", "w", "y", "j", "k", "x"]
genFreq = [" ", "a", "e", "o", "i", "n", "t", "l", "r", "s", "c", "u", "p", "m", "d", "v", "g", "q", "f", "h", "z", "b", "w", "y", "j", "k", "x"]


# Replace our homophones now...
homophones=("G","C","B","M","Z","N")
for phone in homophones:
    ciphertext=Replacer(phone, "&", ciphertext)
    
print(ciphertext)

SymbolList = build(ciphertext, alphabetCharLength)
#print(SymbolList)

DedupedSymbolList = dedupe(SymbolList)
print(DedupedSymbolList)

doubles = findDoubles(DedupedSymbolList, ciphertext)
print(doubles)

FreqCipherText = freq(DedupedSymbolList, ciphertext, alphabetCharLength)

Ordered = sorted(FreqCipherText, key = getKey, reverse = True)
print(Ordered)
print ("Cipher text length is: ", len(ciphertext))
print ("Number of alphabet symbols:", (len(Ordered)))
print ("Frequency distribution", FreqAnalysisCounter(Ordered))
#ReplacedCipherText = Replacer(CharToReplace, CharToReplaceWith, ciphertext)
#print (ReplacedCipherText)

# OK, they are our stats, now for decryption

print(ciphertext)

plainText=""
for character in ciphertext:
    # send each character in our cipher to the decrypt function
    newChar=decrypt(genFreq, Ordered, character)
    # build up our plain text
    plainText += newChar

print(plainText)
