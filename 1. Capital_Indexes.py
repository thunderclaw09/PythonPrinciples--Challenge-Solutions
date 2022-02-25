def capital_indexes(string):
    cap_indexes = []
    current_index = 0
    for i in string:
        if i.isupper() == True:
            cap_indexes.append(current_index)
        current_index+=1
    return cap_indexes
    
print(capital_indexes("HeLlO"))
#Should return [0, 2, 4]