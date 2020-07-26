file_name="min.css"
word=[]
file=open(file_name)
for line in file:
    for w in line.split():
        word.append(w)
print(word)
print(len(word))        