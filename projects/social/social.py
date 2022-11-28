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
        
        if avg_friendships >= num_users:
            print("Could not create graph: The number of users must be greater than the average number of friendships.")
            return
        # Add users
        for i in range(1, num_users + 1):
            self.add_user(f"User {i}")

        # Generate pairs of IDs to make friendships
        total_friendships = avg_friendships * num_users // 2

        friendships_to_create = set()

        while len(friendships_to_create) < total_friendships:

            user1ID = random.randrange(1, num_users + 1)
            user2ID = random.randrange(1, num_users + 1)
            
            # pick a different user ID for user2
            while user1ID == user2ID:
                user2ID = random.randrange(1, num_users + 1)

            # ensure that the same two IDs are not added twice
            smallerID = user1ID if user1ID < user2ID else user2ID
            largerID = user1ID if user1ID > user2ID else user2ID

            friendships_to_create.add((smallerID, largerID))
        
        # Create friendships
        for friendship in friendships_to_create:

            user1ID, user2ID = friendship
            self.add_friendship(user1ID, user2ID)
        
        print(f"\nSuccessfully populated graph with {num_users} users, each with an average of {avg_friendships} friendships.\n")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # make dictionary for visited
        
        # initialize dictionary with path to self
        # later connections will build off of this entry
        visited[user_id] = [user_id]

        # use a queue to keep track of all friends that have not been visited
        q = Queue()
        q.enqueue(user_id)

        while q.size() > 0:

            current_friend_ID = q.dequeue()
            friends_of_current_friend = self.friendships[current_friend_ID]
            
            # process friends of current friend
            for friend_ID in friends_of_current_friend:

                # add new friend to queue and update path
                if friend_ID not in visited:
                    q.enqueue(friend_ID)

                    # make a copy of the path to this friend so far,
                    # and add the current friend's ID
                    path_to_new_friend = list(visited[current_friend_ID])
                    path_to_new_friend.append(friend_ID)
                    # store the path in "visited" to mark the friend as visited
                    visited[friend_ID] = path_to_new_friend

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
