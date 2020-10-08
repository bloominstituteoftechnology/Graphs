# """Print out all of the strings in the following array in alphabetical order, each on a separate line.
# ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process."""

# array = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# array.sort()
# result = ''

# for word in array:
#     print(word, '\n')


#    # ancestors = Graph()
#     # parents_for_child = {}

#     # # Create a graph with IDs as vertices and child->parent relationships as edges
#     # for relationship in ancestors:
#     #     parent = relationship[0]
#     #     child = relationship[1]
#     #     if child not in parents_for_child:
#     #         parents_for_child[child] = set()
#     #     parents_for_child[child].add(parent)

#     # earliest_ancestor = -1

#     # # Perform a Breadth-First Search on the graph and return the last ancestor found
#     # s = Stack()
#     # s.push(starting_node)
#     # while s.size() > 0:
#     #     curr_vertex = s.pop()
#     #     if curr_vertex in parents_for_child:
#     #         parent_with_lowest_ID = None
#     #         for parent in parents_for_child[curr_vertex]:
#     #             if parent_with_lowest_ID is None:
#     #                 parent_with_lowest_ID = parent
#     #             elif parent < parent_with_lowest_ID:
#     #                 parent_with_lowest_ID = parent
#     #             s.push(parent)
#     #         if parent_with_lowest_ID is not None:
#     #             earliest_ancestor = parent_with_lowest_ID

#     # return earliest_ancestor 
            
#     graph = Graph()

#     for vertex_1, vertex_2 in ancestors:
#         graph.add_vertex(vertex_1)
#         graph.add_vertex(vertex_2)

#     for vertex_1, vertex_2 in ancestors:
#         graph.add_edge(vertex_1, vertex_2)

#     target_vertex = None

#     longest_path = 1

#     for vertex in graph.vertices:

#         # vertex = starting_vertex and starting_node = destination_vertex
#         # from imported Graph class DFS method
#         path = graph.dfs(vertex, starting_node)

#         if path:
#             print(path)

#             if len(path) > longest_path:
#                 longest_path = len(path)
#                 target_vertex = vertex

#         elif not path and longest_path == 1:
#             target_vertex = -1

#     return target_vertex
    # queue = Queue()
    # current_node = starting_node
    # relationships = {}
    # for node in ancestors:
    #     if node[1] not in relationships:
    #         relationships[node[1]] = set()
    #     relationships[node[1]].add(node[0])

    # if starting_node in relationships:
    #     queue.enqueue(relationships[current_node])
    # else:
    #     return -1

    # while True:
    #     relations = queue.dequeue()
    #     current_node = min(relations)
    #     if current_node not in relationships:
    #         return current_node
    #     else:
    #         queue.enqueue(relationships[current_node])
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
ll_one = ListNode(2)
ll_one.next = ListNode(4)
ll_one.next.next = ListNode(-3)
ll_two = ListNode(5)
ll_two.next = ListNode(6)
ll_two.next.next = ListNode(-9)
"""
Must be done in linear time and space or better.
Cannot convert linked list into any other data structure.
Must be done in one pass.
Assume Linked lists will not be the same length.
ll_one: 2 => 4 => -3
ll_two: 5 => 6 => -9
7 => 0 => -1 => -1
other problem: 7 => 0 => 8 => None
expected output: 8 => 0 => 7 => None
None <= 7 <= 0 <= 8
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        prev = None
        carry = 0
        while l1 or l2 or carry:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            total += carry
            carry = 0
            if total >= 10:
                total -= 10
                carry += 1
            elif total <= -10:
                total += 10
                carry -= 1
            node = ListNode(total)
            node.next = prev
            prev = node
        return prev
solution = Solution().addTwoNumbers(ll_one, ll_two)
while solution:
    print(solution.val)
    solution = solution.next
"""
test cases:
1. if l1 is None and l2 is None => None
2. if one ll is longer than the other => yes
3. negative numbers => yes
4. if l1 is None but l2 is valid => returns l2
5. two massive linked lists => not a big worry because time complexity is linear
"""