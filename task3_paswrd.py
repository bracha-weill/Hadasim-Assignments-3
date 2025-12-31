import string

def pswrd_check(paswrd: str)->bool:
    if len(paswrd)<8:
        return False
    if not any(c.islower() for c in paswrd):
        return False
    if not any(c.isupper() for c in paswrd):
        return False
    if not any(c.isdigit() for c in paswrd):
        return False
    if not any(c in string.punctuation for c in paswrd):
        return False
    for c in set(paswrd):
        if paswrd.count(c)>2:
            return False
    for i in range(len(paswrd)-2):
        if (ord(paswrd[i+1]) == ord(paswrd[i]) + 1 and ord(paswrd[i+2]) == ord(paswrd[i])+2):
            return False
        
    return True

print(pswrd_check("bracha@1T"))