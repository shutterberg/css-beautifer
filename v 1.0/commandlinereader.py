import sys

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

