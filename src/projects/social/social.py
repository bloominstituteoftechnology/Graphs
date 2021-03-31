import random
from collections import deque


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({self.name})"


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

    def add_friendships(self, user_id, *friends):
        for friend in friends:
            self.add_friendship(user_id, friend)

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
        for i in range(num_users):
            # generates "test_user1", "test_user2", "test_user3"
            self.add_user(f"test_user{i}")

        # Create friendships
        potential_friendships = []
        for user_id in self.users:
            # start with friend after user_id, end with last_id
            for friend_id in range(user_id + 1, self.last_id + 1):
                potential_friendships.append((user_id, friend_id))

        # shuffle up friendships!
        random.shuffle(potential_friendships)

        # divide by two to avoid duplicates
        for i in range((num_users * avg_friendships) // 2):
            friendship = potential_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_shortest_path(self, starting_user, destination_user):
        """Return the shortest friend path from starting user to destination user"""

        # using collections.deque as a Queue (cuz that's better than writing a class!)
        # deque.append(value) will add the value at the end of the list
        # deque.popleft() will return the value at the beginning of the list
        q = deque()

        # add path with just our starting user to the end of our queue
        # our queue will hold a collection of possible paths from starting_user to somewhere
        # (hopefully destination_user)
        q.append([starting_user])

        # visited will be a set with all visited nodes (or "vertices" or "users")
        visited = set()

        # while our queue is not empty
        while len(q) > 0:
            path = q.popleft()  # get the least-recently added path
            friend = path[-1]  # the last vertex in our path
            # if friend has not yet been visited
            if friend not in visited:
                # if friend is our destination, our path is complete!
                if friend == destination_user:
                    # so return it
                    return path

                # if we're here then friend is not our destination_user
                visited.add(friend)

                # add all next possible paths to our queue
                for next_friend in self.friendships[friend]:
                    new_path = path.copy()  # make a copy of our path
                    new_path.append(next_friend)  # add next friend to our copied path
                    q.append(new_path)  # add this possible path to our queue so we can re-iterate!

    def get_all_social_paths(self, user_id):
        """
        Find the shortest path to each friend in user_id's extended network

        Return a dictionary containing every user in that user's extended network with
        the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """

        # this solution is a BFS within a DFS.
        # DFS through every friend, friend of a friend, friend of a friend of a friend, etc.
        # to obtain the full extended network. that's how we get our KEYS
        #
        # use a deque as stack. append adds to end, pop takes from end. FIFO
        stack = deque()
        # start with one path that only contains our user_id.
        # the stack will contain a collection of paths from user_id to somewhere
        stack.append([user_id])
        friend_paths = {}  # friend_paths dict (visited dict)
        while len(stack) > 0:  # while stack is not empty
            path = stack.pop()  # get the MOST RECENTLY ADDED path
            friend = path[-1]  # take the last friend from path

            # if friend not yet visited
            if friend not in friend_paths:
                # then make friend a key in our dict, with a value that is the shortest path from
                # given user TO this friend
                # self.get_shortest_path will use a BFS to find the shortest path from user_id to friend
                friend_paths[friend] = self.get_shortest_path(user_id, friend)

                # for every possible next friend in path
                for next_friend in self.friendships[friend]:
                    new_path = path.copy()  # make a copy of our path
                    new_path.append(next_friend)  # add our next friend to that path
                    stack.append(new_path)  # add this next possible path to our stack

        return friend_paths  # return our visited friends with each shortest path


graph_01 = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return f"Vertex({self.value})"


def traverse(node, path, out_matrix):
    path.append(node.value)
    if len(node.edges) < 1:
        out_matrix.append(path)
    for edge in node.edges:
        traverse(edge, path.copy(), out_matrix)


def find_paths(graph):
    all_paths = []

    if not graph:
        return []

    # initialize a vertex with the value of index for each index in graph
    nodes = [Vertex(i) for i in range(len(graph))]

    # for each node, sublist in a joined iteration of nodes and graph
    for node, graph_sublist in zip(nodes, graph):
        node.edges = [nodes[index] for index in graph_sublist]

    traverse(nodes[0], [], all_paths)
    return all_paths


def find_paths(graph):
    all_paths = []

    if not graph:
        return []

    # initialize a vertex with the value of index for each index in graph
    nodes = [Vertex(i) for i in range(len(graph))]

    # for each node, sublist in a joined iteration of nodes and graph
    for node, graph_sublist in zip(nodes, graph):
        node.edges = [nodes[index] for index in graph_sublist]

    traverse(nodes[0], [], all_paths)
    return all_paths


def find_paths_a_to_b(graph):
    tracker = []
    if not graph:
        return tracker

    # node_path(0, []) -->
    #  node_path(2, [0]), node_path(1, [0]),
    #    node_path(3, [0, 1]),
    #
    def node_path(node, path):  # 2, [0]
        new_path = path + [node]  # new_path = [0] + [2] => new_path = [0, 2],
        for i in graph[node]:  # 3
            print(f"IN FOR LOOP {(i, new_path)}")
            node_path(i, new_path)

        if node == len(graph) - 1:
            print(f"node == destination")
            print(f"current_tracker: {tracker}")
            tracker.append(new_path)
            print(f"after adding: {tracker}")

        print(f"RETURNING TRACKER ---- {tracker}")
        return tracker

    return node_path(0, [])


if __name__ == '__main__':
    all_paths = find_paths_a_to_b([[1, 2], [3], [3], []])
    print(all_paths)
    # randomly populated graph
    # print("Randomly populated Graph")
    # sg = SocialGraph()
    # sg.populate_graph(10, 2)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    #
    # # graph from readme example
    # print("\nGraph from README")
    # sg_readme = SocialGraph()
    # sg_readme.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5},
    #                          9: {4}, 10: {1, 2, 6}}
    # sg_readme.last_id = 10
    # print(sg_readme.friendships)
    # connections = sg_readme.get_all_social_paths(1)
    # print(connections)
    # expected = {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
    # result = expected == connections
