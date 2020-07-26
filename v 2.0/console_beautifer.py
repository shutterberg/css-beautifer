import tempfile,os,shutil

ff =open("temp.txt","w+")
lenw=0
def beautify(word):
    for letter in word:           #loops to all lettersin a word to find {,},;
        lenw=0                    #lenw lenght of each word reset at start of every loop
        if(letter=='{'or letter=='}'):
            if(letter=='{'):
                ff.write('\t')
                ff.write(letter[lenw])
                ff.write('\n')
                ff.write('\t')
                lenw+=1
            elif(letter=='}'):
                ff.write('\n')
                ff.write(letter[lenw])
                ff.write('\n')
                lenw+=1  
        elif(letter==';'):
            ff.write(letter[lenw])
            ff.write('\n')
            ff.write('\t')   
        elif(lenw==0):
            ff.write(letter[lenw])
        else:
            ff.write(letter[lenw])
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
        beautify(word)                                     #calling beautify to beautify the css
ff.close()
shutil.copy('temp.txt',bfile)
os.remove('temp.txt')
print("File beautifed")