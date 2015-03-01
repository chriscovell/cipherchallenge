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
    specFreq = [[0 for j in range(2)] for i in range(26)]
    for x in range(0, (len(string)), 2):
        count = 0
        y = string[x:x+2]
        #print(y)
        #Built.append(y)
    print(Built)
    return(Built)

def freq(alphabet, string):
    for symbol in alphabet:
        count = 0
        print(symbol)
    return()

SymbolList = build(cleaner(ciphertext))
#print(SymbolList)
freq(SymbolList, ciphertext)

def getKey(item):
    
    return item[1]