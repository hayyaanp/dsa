def number_of_tokens(expiryLimit, commands):
    
    tokens = {}
    
    for cmd in commands:
        [action, token_id, timestamp] = cmd   
    
        # create
        if action == 0:
            tokens[token_id] = expiryLimit + timestamp
        
        # reset
        elif action == 1:
            if token_id in tokens and tokens[token_id] > timestamp:
                tokens[token_id] = expiryLimit + timestamp
                
    
    current_time = commands[-1][2]
    
    count = 0
    for expiry in tokens.values():
        if expiry > current_time:
            count += 1
    
    return count        

print(number_of_tokens(3, [[0, 1, 1], [1, 1, 4], [1, 2, 5]]))