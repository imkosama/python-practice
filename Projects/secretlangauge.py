# Secret code language
# coding
# If the word contains atleast 3 characters,remove the first letter and append it at the end
# now append 3 random character at starting and at the end
# else:
# simply reverse the string

# decoding
# if word contain 3 character revrese it
# else:
# remove 3 random character form start and at the end .Now remove the last letter

from random import choices
import string
st = input("Enter the message : ")
words = st.split(" ")
coding =input(" 1 for coding or 0 for decoding : ")
coding=True if(coding=="1") else False
if coding:
    nwords = []
    for word in words:
        
        if (len(word) >= 3):
             s=(string.ascii_lowercase)
             r1 ="".join(choices(s,k=3))
             r2 ="".join(choices(s,k=3))
             newst = r1 + word[1:] + word[0] + r2
             nwords.append(newst)
        else:
            nwords.append(word[::-1]) # reverse the string
    print(" ".join(nwords))
 
 
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            newst=word[3:-3] # the indexing will start from 3 and goes to -4 it will not consider index value of -3 
            newst=newst[-1]+newst[:-1]
            nwords.append(newst)
        else:
            nwords.append(word[::-1])
    print((" ".join(nwords)))
              
              
