import random

msg=input("Enter the message: ")
words=msg.split(" ")
coding=input("Press 1 for Coding OR 0 for Encoding: ")
coding=True if(coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            passwords = ["ktp", "snp", "poi", "qwr", "uyz", "zpz", "npm", "tty", "kkt", "pwd", "aab", "aap", "opp"]
            password1=random.choice(passwords)
            password2 = random.choice(passwords)
            newst=password1+word[1:]+word[0]+password2
            nwords.append(newst)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            newst = word[3:-3]
            newst = newst[-1] + newst[:-1]
            nwords.append(newst)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
