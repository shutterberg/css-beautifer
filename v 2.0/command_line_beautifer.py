import sys,tempfile,os,shutil

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
ff.close()
shutil.copy('temp.txt',bfile)
os.remove('temp.txt')
print("File beautifed")                   