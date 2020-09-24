import copy
import random
import time

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
            return False
            
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
            
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates(self, arr):
        copy_arr = list(arr)
        # iterate over the array
        for idx in range(len(copy_arr)):
            # choose a random index
            rand_index = random.randint(0, len(copy_arr) - 1)
            # swap the current item with that random index
            copy_arr[idx], copy_arr[rand_index] = copy_arr[rand_index], copy_arr[idx]

        return copy_arr

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        if num_users < avg_friendships:
            return

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        # you could create a list with all possible friendship combinations
        ### class solution
        all_friend_combos = []
        for person in range(1, num_users):
            for friend in range(person + 1, num_users + 1): # start 1 higher so we don't get reverse combo
                all_friend_combos.append((person, friend))
        ## [(1, 2), (1,3), (1,4), (2,3), (2,4), (3,4)]

        # shuffle the list
        shuffled_combos = self.fisher_yates(all_friend_combos)

        # grab the first N elements from the list
        total_friendships = num_users * avg_friendships
        elements_needed = total_friendships // 2
        combos_to_make = shuffled_combos[:elements_needed]
        
        # then loop over the list and call add_friendship
        for friendship in combos_to_make:
            self.add_friendship(friendship[0], friendship[1])


        # possible_friendships = []

        # for user in self.users:
        #     for friend in range(user + 1, self.last_id + 1):
        #         possible_friendships.append((user, friend))

        # random.shuffle(possible_friendships)

        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])


    def linear_populate_graph(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        total_friendships = num_users * avg_friendships
        ## stop at required amount
        total_friendships_made = 0
        while total_friendships_made < total_friendships:
            # to run in linear time
            # pick two random user_ids
            friend_1 = random.randint(1, num_users)
            friend_2 = random.randint(1, num_users)
            ## try to make them friends
            friendship_made = self.add_friendship(friend_1, friend_2)
            ## track number of friendships made
            if friendship_made:
                total_friendships_made += 1
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        
        Traversal problem. 
        
        "Shortest path" is the hint to use BFT
        If we have request to use a "recursive" approach --> DFT
        """
        ### class solution
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        
        q.enqueue([user_id])

        while q.size() > 0:
            current_path = q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path

                friends = self.friendships[current_user]

                for friend in friends:
                    copy_path = list(current_path)
                    copy_path.append(friend)
                    q.enqueue(copy_path)

        return visited
        
        
        # queue = Queue()
        # queue.enqueue([user_id])

        # while queue.size() > 0:
        #     current_path = queue.dequeue()
        #     current_vertext = current_path[-1]
            
        #     if current_vertext not in visited:
        #         visited[current_vertext] = current_path

        #     for n in self.friendships[current_vertext]:
        #         copy_path = current_path.copy()
        #         copy_path.append(n)
        #         queue.enqueue(copy_path)

        # return visited


if __name__ == '__main__':
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(1000, 5)
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    sg.linear_populate_graph(1000, 5)
    end_time = time.time()
    print(end_time - start_time)

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    ## connection dict holds everyone in 1's extended social network

    # print(f'Percent of users in extended social network: {len(connections) / 1000 * 100}%')