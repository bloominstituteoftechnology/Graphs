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

        # Add users
        for i in range(0, num_users):
            self.add_user(f"user  {i}")
        
        # create friendships 
        nw_friends = [] #[(user_sally, firend_joe)]
        #  generate all possible friendship combos 
        for user in self.users:
            for friend in range(user + 1, self.last_id + 1):
                nw_friends.append((user, friend))
        # randomize the above array 
        random.shuffle(nw_friends)
            
        

        # Create friendships
        n_users = num_users * avg_friendships // 2
        for i in range(n_users):
           relationship = nw_friends[i]
        #    relationship = user, friend
           user = relationship[0]
           friend = relationship[1]
           self.add_friendship(user, friend)
           
    
    
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([user_id])
        
        while queue.size() > 0:
            path = queue.dequeue()
            cur_vertex = path[-1]
            
            if cur_vertex not in visited:
                visited[cur_vertex] = path 
                
                friendships = self.friendships[cur_vertex]         
                for friend in friendships:
                    # copy the path array 
                    new_path = path.copy()
                    new_path.append(friend)
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
