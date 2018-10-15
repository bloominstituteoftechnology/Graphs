# This can be used to run in Python Tutor to see what's going on

def dfs(curr_vert, target_value, visited=[]):
    adjList = {
    '0':['1','2','3'],
    '1':['4','5'],
    '2':['6','7'],
    '3':['8','9'],
    '4':[],
    '5':[],
    '6':[],
    '7':[],
    '8':[],
    '9':[]
    }
    visited.append(curr_vert)
    # print(adjList[int(curr_vert)])
    if curr_vert == target_value:
        return True
    print(curr_vert)
    for child_vert in adjList[curr_vert]:
        if child_vert not in visited:
            if dfs(child_vert, target_value, visited):
                return True
    return False

print(dfs('0','22'))