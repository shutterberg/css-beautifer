import sys

lenw=0
def beautify(word):
    for letter in word:
        lenw=0
        if(letter=='{'or letter=='}'):
            if(letter=='{'):
                print('\t',letter[lenw],end="")
                print('\n')
                print('\t',end="")
                lenw+=1
            elif(letter=='}'):
                print('\n')
                print(letter[lenw],end="")
                print('\n')
                lenw+=1  
        elif(letter==';'):
            print(letter[lenw],end="")
            print('\n')
            print('\t',end="")   
        elif(lenw==0):
            print(letter[lenw],end="")
        else:
            print(letter[lenw],end="")
            lenw+=1

def iscss(checkbfile):
    ext=checkbfile.split('.')
    ext=ext[-1].lower()
    if(ext=="css"):
        return True
    else:    
        return False     

bfile=str(sys.argv[1])
if(iscss(bfile)):
    print("Opening "+bfile)

word=[]
file=open(bfile)
for line in file:
    for w in line.split():
        word.append(w)
for word in word:        
        beautify(word)           