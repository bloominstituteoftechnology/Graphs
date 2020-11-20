
import random


class User:
    def __init__(self, name):
        self.name = name

    import random


class SocialGraph:
    def __init__(self):
        self.last_id = 0  # the number of users you currently have
        self.users = {}  # users with attribs, wont use
        self.friendships = {}
        # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {
        # 8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}  # adjacency list

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

    def get_friends(self, user_id):
        return self.friendships[user_id]

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def bft_path(self, start_vertex):
        q = []
        visited = {}
        path = [start_vertex]
        q.append(path)
        # result = {}

        while len(q) > 0:
            # print("queue", q)
            new_path = q.pop(0)
            vertex = new_path[-1]
            # print("vertex", vertex)

            if vertex not in visited:
                visited[vertex] = new_path
            # if vertex == start_vertex:
            #     result[start_vertex] = new_path
                # if len(self.get_friends(vertex)) == 0:
                #     all_paths.append(new_path)
                # else:
                for neighbor in self.get_friends(vertex):
                    # if neighbor in new_path:
                    #     result[vertex] = new_path
                    # else:
                    copy_path = new_path + [neighbor]
                    q.append(copy_path)
        return visited

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
        for user in range(num_users):
            self.add_user(user)
        # Create friendships
        total_friendships = avg_friendships * num_users
        # create a list of all possible friendships
        friendship_combos = []

        for user_id in range(1, num_users + 1):
            for friend_id in range(user_id+1, num_users+1):
                friendship_combos.append((user_id, friend_id))

        # shuffle the list,
        self.fisher_yates_shuffle(friendship_combos)
        # then grab first n elements from the list
        # print("frinedshipt combos", friendship_combos)
        friendships_to_make = friendship_combos[:(total_friendships // 2)]
        # only create friendships where user1< user2
        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's

        The key is the friend's ID and the value is the path.
        extended network with the shortest friendship path between them.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = []
        path = [user_id]
        q.append(path)
        # result = {}

        while len(q) > 0:
            # print("queue", q)
            new_path = q.pop(0)
            vertex = new_path[-1]
            # print("vertex", vertex)

            if vertex not in visited:
                visited[vertex] = new_path
            # if vertex == start_vertex:
            #     result[start_vertex] = new_path
                # if len(self.get_friends(vertex)) == 0:
                #     all_paths.append(new_path)
                # else:
                for neighbor in self.get_friends(vertex):
                    # if neighbor in new_path:
                    #     result[vertex] = new_path
                    # else:
                    copy_path = new_path + [neighbor]
                    q.append(copy_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 1000
    avg_friendships = 5
    sg.populate_graph(num_users, avg_friendships)
    # print(sg.friendships)
    # print("get friends", sg.get_friends(1))
    # print(sg.bft_path(1))
    connections = sg.get_all_social_paths(1)
    # print(connections)

# percentage of other users in extended social network
    # NUMBER OF  people we visited/ total number of peope
    print(len(connections)/num_users)

# average degree of separation --> average steps we took to visit someone
# average length of the path
    total_path_lenghths = 0

    for key, value in connections.items():
        total_path_lenghths += len(value)

    average_path_length = total_path_lenghths/len(connections)
    print(average_path_length)