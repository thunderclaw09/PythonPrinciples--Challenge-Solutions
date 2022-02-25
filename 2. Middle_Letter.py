def mid(string):
    length = len(string)
    remainder = length % 2
    if remainder == 0:
        return ("")
    else:
        middle = int((length/2) - 0.5)
        return string[middle]
        
print(mid("abc"))
print(mid("aaaa"))
#Should return b, <blank>