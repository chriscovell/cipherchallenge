# Start of stage 4
#open text file
r = open("stage4_ciphertext", "r")
ciphertext = r.read()
#frequency of letters
genFreq = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]

#frequency function
def freq(string):
    for alphabet in range(65, 91):
        print(chr(alphabet))
        count = 0
        for x in string:
            if x == chr(alphabet):
                count = count+1
            print(count)
            specFreq[alphabet-65]=(chr(alphabet),count)
            return(specfreq)