statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dictionary):
    online = 0
    for i in dictionary:
        if dictionary[i] == "online":
            online+=1
    return online
    
print(online_count(statuses))

#Should return 2