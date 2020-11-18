import random
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        # maps ID's to user objects (lookup table for user objects given id's)
        self.users = {}
        # Adjency List
        # Maps users to a list of other users (who are their friends)
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
        # Add users
        for i in range(0,num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all possible friendships
        # Avoid duplicate friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # Randomly selected X friendships
        # thr forula for X is num_users * avg_friendships // 2

    def get_neighbors(self, vertex):
        neighbors = []
        return self.friendships[vertex]

    def bft(self, starting_vertex, looking_for):
        # Create an empty queue an enqueue the starting vertex
        path_dict = {}
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visitied verticies
        visited_set = set()
        first = True
        neighbor_count = 0
        path = []


        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex (deque from queue)
            current_vertex = queue.dequeue()
            print(current_vertex)
            # Check if the current vertex has been visited:
            if first:
                first = False
                path.append(current_vertex)
                visited_set.add(current_vertex)
                path_dict[current_vertex] = path
                for neighbor in self.get_neighbors(current_vertex):
                    queue.enqueue(neighbor)
                    print(" -- ")
                    print(f"Neighbor {neighbor} queue {queue.queue}") 
                    print(" -- ")
                    neighbor_count += 1
                    path.append(neighbor)
                    path_dict[neighbor] = path

            else:
                if current_vertex not in visited_set:
                    visited_set.add(current_vertex)
                    # check to see if it's in the dict
                    if current_vertex in path_dict:
                        # check to see if all neighbors are in path dict
                        for neighbor in self.get_neighbors(current_vertex):
                            if neighbor in path and visited_set:
                                print("")
                                # queue.enqueue(neighbor)
                                # if neighbor in path_dict:
                                #     queue.enqueue(neighbor)

                                # else:
                                #     path.append(neighbor)
                                #     path_dict[neighbor] = path
                                #     queue.enqueue(neighbor)
                            elif neighbor in path and neighbor not in visited_set:
                                    queue.enqueue(neighbor)
                            
                            else:
                                path.append(neighbor)
                                path_dict[neighbor] = path
                                queue.enqueue(neighbor)
                    else:
                        for neighbor in self.get_neighbors(current_vertex):
                            if neighbor in path_dict:
                                print("")
                            else:
                                path.append(neighbor)
                                path_dict[neighbor] = path
                                queue.enqueue(neighbor)


                    # print(current_vertex)
                    # visited_set.add(current_vertex)
                    # if current_vertex in path:
                    #     print("")
                    # else:    
                    #     path.append(current_vertex)
                    #     path_dict[current_vertex] = path
                    # # path_dict[current_vertex] = path
                    # for neighbor in self.get_neighbors(current_vertex):
                    #     if neighbor in path:
                    #         print("")
                    #         # path_dict[current_vertex] = path
                    #     else:
                    #         path.append(neighbor)
                    #         queue.enqueue(neighbor)
                    #         # path_dict[current_vertex] = path
                    #         # print(" -- ")
                    #         # print(f"Neighbor {neighbor} queue {queue.queue}") 
                    #         # print(" -- ")
                    #         neighbor_count += 1

                    


        # return path

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        need_to_visit = []
        visited = {
            # store the user as the key and the path to the user as the value

        }  # Note that this is a dictionary, not a set
        # append the user_id and path like (1: [1])
        # need_to_visit.append(user_id)
        # # find all connections (friends)
        # for friend in sg.friendships:
        #     if user_id in sg.friendships[friend]:
        #         need_to_visit.append(friend)
                
        self.bft(user_id, sg.friendships[user_id])
        # for friend in need_to_visit:
        #     path = self.bft(friend)
            

        # bfs to return all the paths to friends
        print(need_to_visit)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(5, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
