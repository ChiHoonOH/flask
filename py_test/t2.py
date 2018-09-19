text='1234' #=> 1**4

def change(text):   
    return(text[:1]+'*'*len(text[1:-1])+text[-1:])

change(text)

