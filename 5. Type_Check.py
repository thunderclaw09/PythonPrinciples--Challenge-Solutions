intExample = 12
def only_ints(int1, int2):
    if type(int1) == type(intExample):
        if type(int2) == type(intExample):
            return True
        else:
            return False
    else:
        return False
        
print(only_ints(234, 2345))
# Should return True