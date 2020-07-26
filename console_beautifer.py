import sys

lenw=0
def beautify(word):
    for letter in word:           #loops to all lettersin a word to find {,},;
        lenw=0                    #lenw lenght of each word reset at start of every loop
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

def iscss(checkbfile):                  #to validate extension
    ext=checkbfile.split('.')
    ext=ext[-1].lower()                 #to collet extension
    if(ext=="css"):
        return True
    else:    
        return False     

bfile=input("Enter file name to be beautifed: ")
if(iscss(bfile)):
    print("Opening "+bfile)

word=[]                                                     #word are saved in this list
file=open(bfile)
for line in file:
    for w in line.split():                                 #spliting words of each line                             
        word.append(w)                                     #appening words into the list     
for word in word:        
        beautify(word)                                      #calling beautify to beautify the css            