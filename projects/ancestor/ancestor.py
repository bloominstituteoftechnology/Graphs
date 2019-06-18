class FamilyTree:
    def __init__(self):
        self.people = {}

    def add_person(self, p):
        if p not in self.people:
            self.people[p] = (set(), set())

    def add_relation(self, parent, child):
        if parent not in self.people:
            self.people[parent] = (set(), set())
        if child not in self.people:
            self.people[child] = (set(), set())
        self.people[parent][0].add(child)
        self.people[child][1].add(parent)

    def find_ancestor(self, start):
        queue = []
        dist = {}

        queue.append(start)
        dist[start] = [start]
        longest_dist = 0
        longest_ind = start
        
        while queue:
            s = queue.pop(0)
            for c in self.people[s][1]:
                if c not in dist:
                    queue.append(c)
                    dist[c] = dist[s]+[c]
                elif len(dist[c]) > len(dist[s]) + 1:
                    dist[c] = dist[s] + [c]
                if len(dist[c]) > longest_dist:
                    longest_dist = len(dist[c])
                    longest_ind = c
        if longest_dist != 0:
            return longest_ind
        return -1

def ancestor():
    tree = FamilyTree()

    start = input()
    tree.add_person(start)
    print()
    
    pair = input()
    while pair != "":
        vals = pair.split(" ")
        if len(vals) > 1:
            tree.add_relation(vals[0], vals[1])
        else:
            return -1
        pair = input()
    return tree.find_ancestor(start)


print(ancestor())
