#open file
r=open('stage2_ciphertext','r')

cipherText=r.read()

print cipherText

# we know this is a Caesar shift
# so just use ascii values to shift
# A=65

for shift in range(1, 26):
    print "shift",shift
    for character in cipherText:
        val=ord(character)
        if val+shift>90:
            jiggle=val+shift-26
        else:
            jiggle=val+shift
        if val<65 or val>91:
            jiggle=val
        print chr(jiggle),
    print # to get the new line