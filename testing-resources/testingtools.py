

def compare_doubles(a, b):
    return abs(a-b) < 0.0001
    
    
def compare_unsorted_lists(a,b):
    if a == None or b == None:
        return a == b
        
    if len(a) != len(b):
        return False
        
    for i in a:
        if a.count(i) != b.count(i):
            return False
            
    return True
    
def compare_sorted_lists(a,b):
    if a == None or b == None:
        return a == b
        
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != a[b]:
            return False
    return True
    

def bin_results(a):
    result = []
    
    cur_bin = [a[0]]
    for i in range(1, len(a)):
        entry = a[i]
        if abs(entry["score"] - a[i-1]["score"]) < 0.00001:
                cur_bin.append(entry)
        else:
            result.append(cur_bin)
            cur_bin = [entry]
    result.append(cur_bin)
    return result
    
def find_match_index(entry, a):
    for i in range(len(a)):
        e = a[i]
        if e["title"] == entry["title"] and e["url"] == entry["url"]:
            return i
    return -1
    
def compare_binned_results(a,b):        
    if len(a) != len (b):
        return False
        
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            return False
        
        while len(a[i]) > 0:
            entry = a[i].pop()
            match_index = find_match_index(entry, b[i])
            if match_index >= 0:
                b[i].pop(match_index)
            else:
                return False
                
    return True
        
def compare_search_results(a, b):
    if len(a) == 0 and len(b) == 0:
        return True
    
    a = bin_results(a)
    b = bin_results(b)
    return compare_binned_results(a,b)
    


    