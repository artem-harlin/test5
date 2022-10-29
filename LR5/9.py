def Capitalize(S):
    d = ''
    for i in range(len(f)):
        c = f[i]
        if c.isalpha() and i == 0:
            d += c.upper()
        elif c.isalpha() == True and f[i - 1].isalpha() == False:
            d += c.upper()
        elif c.isupper() == True and f[i - 1].isalpha() == True:
            d += c.lower()
        else:
            d += f[i]
    return(d)
S = input()
print (Capitalize(S))
