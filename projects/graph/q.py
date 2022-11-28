# from collections import deque

# my_q = deque()

# my_q.append(5)
# my_q.append({23,33})
# print(my_q)
# my_q.pop()
# print(my_q)


def permute(s):
    out = []
    
    
    #BaseCase
    if len(s) == 1:
        out = [s]
    else:
        
        for i, let in enumerate(s):
            
            for perm in permute(s[:1] +s[i+1:]):
                print('perm is', perm)
                
                out +=[let+perm]
    return out            


permute('abc')