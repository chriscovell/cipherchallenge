#open file
r=open('stage1_ciphertext','r')

cipherText=r.read()

#genFreq=["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
genFreq=["e","t","a","h","n","o","s","i","r","d","l","g","c","w","f","k","m","p","u","b","v","y","j","x","q","z"]

def freq(string):
    # count each character and return an array of the specific frequency distribution
    # Use ascii values for each letter, A=65
    #chr(97)  = "a"
    specFreq = [[0 for j in range(2)] for i in range(26)]
    # go through each letter of the alphabet
    for alphabet in range(65, 91):
        #print chr(alphabet)
        count=0
        # go through each letter of the string
        for x in string:
            if x==chr(alphabet): # and look to see if there is a match
                count=count+1
        # print count
        # return a list of tuples, most frequent first
        specFreq[alphabet-65]=(chr(alphabet),count)
    return specFreq

def getKey(item):
    # this is a funny thing I need to do in python in order to use sorted
    return item[1]

def decrypt(baseFreq, ourFreq, character):
    # find our character in ourFreq map
    
    for c in range(0,26):
        tup=ourFreq[c]
        if tup[0]==character:
            return baseFreq[c]
    # return the appropriate character out of the baseFreq list
    return character

cipherTextFreq = freq(cipherText)
#print cipherTextFreq

orderedCipherTextFreq = sorted(cipherTextFreq, key=getKey, reverse=True)
#print orderedCipherTextFreq

print cipherText

plainText=""
for character in cipherText:
    # send each character in our cipher to the decrypt function
    newChar=decrypt(genFreq, orderedCipherTextFreq, character)
    # build up our plain text
    plainText=plainText+newChar
    
print plainText