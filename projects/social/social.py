import random 
from queue import  Queue

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({repr(self.name)})"

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

   

    def add_friendship(self, user_id, friend_id): # this is the edge
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            #print("WARNING: You cannot be friends with yourself")
            return -1
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:

            #print("WARNING: Friendship already exists")
            return -1
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return 1 # this means the function was succesfull

    def add_user(self, name): # this is the node
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) #dict of key--id, and val--userName
        self.friendships[self.last_id] = set() # dict of key--id, and val--set to hold other users

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

        # Add users -- doing a loop through the number of users
        for i in range(num_users):
            self.add_user(f"User {i}")


        # # Create friendships
        possibleFriendships = []

        # for user_id in self.users:
        for user_id in self.users:
            # looping through the other users to make friends will
            # start at the id just above the current id so that
            # we are not friends with ourselves
            for friend_id in range(user_id +1, self.last_id + 1):
                possibleFriendships.append((friend_id, user_id)) 
        # will now use the random shuffle to shuffle some of the names
        random.shuffle(possibleFriendships)
        

        for i in range(num_users * avg_friendships // 2):
            # adding the friendships
            self.add_friendship(possibleFriendships[i][0], possibleFriendships[i][1])
        

    # This is the second version of the populate graph which will hopefully
    # have a better time complexity
    def populate_graph_2(self, num_users, avg_friendships):
        # will make it to reset the graph
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # what are the total number of friendships that we want
        totalFriendshipsNeeded = num_users * avg_friendships
        totalFrienships = 0
        # Add users -- doing a loop through the number of users
        for i in range(num_users):
            self.add_user(f"User {i}")
        # doing second loop that will choose two random
        while totalFrienships < totalFriendshipsNeeded:
            user1_id = random.randint(1, self.last_id)
            user2_id = random.randint(1, self.last_id)

            result = self.add_friendship(user1_id, user2_id)
            if result == 1:
                totalFrienships+=2 # adding another friendship eventually causing the exit of the loop
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # to find the shortest path we need to to a breadth first search
        # We will loop through doing the bft and then add the path to the 
        # dictionary visited if is not in the dictionary already.
        # 
        
        myQueue = Queue()
        if user_id not in self.users: # looking in the keys
            
            raise("That user id is not part of the social network")

        path = [user_id]
        # add to the Queue
        myQueue.put(path)

        # doing the while loop
        while myQueue.qsize() > 0:
            # dequeue
            curPath = myQueue.get()
            if curPath[-1] not in visited:
                # added to the visited
                visited[curPath[-1]] = curPath
                # will now get the neighbors of the curPath[-1]
                for friend in self.friendships[curPath[-1]]:
                    newPath = curPath[:]
                    newPath.append(friend)
                    # putting it in the queue
                    myQueue.put(newPath) 


        return visited


if __name__ == '__main__':

    theUsr = 1
    sg = SocialGraph()

    #sg.populate_graph(100, 2)
    sg.populate_graph_2(100, 2)
    print("Printing the users in the social network")
    print(sg.users)
    print("\nPrinting the friendships that are in the social network")
    print(sg.friendships)
    connections = sg.get_all_social_paths(theUsr)
    print("\nPrinting the connection ")
    print(connections)
