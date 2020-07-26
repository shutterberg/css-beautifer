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
    

file_name="min.css"
word=[]
file=open(file_name)
for line in file:
    for w in line.split():
        word.append(w)
for word in word:        
        beautify(word)   