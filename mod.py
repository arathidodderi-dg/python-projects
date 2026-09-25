def target_search(target,searchlist):
    for i,value in enumerate(searchlist):
        if value == target:
            return i+1
    return -1   

    
   