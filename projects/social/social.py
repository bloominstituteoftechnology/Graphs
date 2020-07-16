#from projects/graph/util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # add users
        for i in range(num_users):
            self.add_user(f'User {i}')

        # create friendships list
        possible_friendships = []

        # for each friend-user combination, place a tuple in possible_friendships 
        for user_id in self.users:
            for friend_id in range(user_id + 1,self.last_id + 1):
                possible_friendships.append([user_id, friend_id])

        import random
        # shuffle the possible friendships so the order isn't biased towards towards the early users
        random.shuffle(possible_friendships)

        # add friendships
        # designate a certain number of friendships determined by avg friendships per total users
        for i in range(num_users * avg_friendships // 2):
            # this sets the friendship variable to a premade possible friendship
            friendship = possible_friendships[i]
            # then we add this friendship to the friendship dictionary that defines the graph
            # with the first tuple value as the key and the second as the value
            self.add_friendship(friendship[0],friendship[1])
            



    

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
        
    #     # need to keep track of each path and the minimum path length
    #     # create an empty queue
    #     q = {}

    #     # create a set to store the visited nodes
    #     visited = set()

    #     # init enqueue the starting node
    #     q.enqueue([starting_vertex])

    #     while q.size() > 0:
            
    #         # Dequeue the first item
    #         q_path = q.dequeue()
    #         v = q_path[-1]
    #         #print('q',q_path)

    #                  # SELF.VISITED NEEDS TO BE RESET OR INITIATED ELSEWHERE
    #         # If it's not been visited:
    #         if v not in visited:
                
    #             if v == destination_vertex:
                    
    #                 # IF SO, RETURN PATH
    #                 return q_path
    #             # Mark as visited (i.e. add to the visited set)
    #             visited.add(v)
                
    #             # Add all neighbors to the queue
    #             for next_vert in self.get_neighbors(v):
    #                 # copy the path
    #                 temp_path = list(q_path)
    #                 temp_path.append(next_vert)
                    
    #                 q.enqueue(temp_path)

    #     return None

    
    

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """     #each user v       v       each path V          V
        # output example- {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        visited = {}  # Note that this is a dictionary, not a set
        # Need to do a bfs using the user id
        # first step is to traverse the graph and record all the vertices as keys in visited using bft
        # then take those keys and use bfs on each, using user_id as the starting node and and the key as
        # the destination node

        # Modification of BFT
        # create an empty dict
        # q = Queue()
        q = []

        # init enqueue the starting node
        q.append(user_id)

        while len(q) > 0:
            # Dequeue the first item
            v = q.pop(0)
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited[v] = []

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the queue
                for next_vert in self.friendships[v]:
                    q.append(next_vert)

        # once visited is filled, then we start the bfs
        #print('vv',visited)
        possible_paths = {}
        #run a bfs for each key in visited
        for v in visited:
            possible_paths[v] = []
            
            if v == user_id:
                visited[v] = [user_id]

            path = []
            while len(path) < len(visited):

                # Add all neighbors to the queue
                for next_vert in self.friendships[v]:
                    print(possible_paths[v])
                    # copy the path
                    # temp_path = list(path)
                    # temp_path.append(next_vert)
                    # add path to possible_paths
                    path.append(next_vert)

                    possible_paths[v].append(path)  # HAVE TO USE QUEUE OR STACK, THEY ENSURE THE NEIGHBORS
                                                    # FOLLOW THE CORRECT ORDER WHEN LOOPING 

                    if v == path[-1]:
                    
                    # IF SO, RETURN PATH
                        visited[v] = path
                        break

        # for x in visited:
        #     bfs(user_id, x)
        #     visited[x].add(path)
        
        print('pct of total users in network', len(visited[1])/len(visited))
        print('degrees of separation', len(visited[1]) - 1)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('fships',sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('social paths',connections)
