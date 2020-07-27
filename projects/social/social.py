import random
from queue import SimpleQueue


class User:
    """
    Represents a user of a friendship-based social networking site.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SocialGraph:
    """
    Represents a friendship-based social networking site.
    """
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            raise ValueError("WARNING: You cannot be friends with yourself.")
        elif (friend_id in self.friendships[user_id] or
              user_id in self.friendships[friend_id]):
            raise ValueError("WARNING: Friendship already exists.")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.last_id += 1
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments.

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Check argument validity.
        if avg_friendships > num_users - 1:
            raise ValueError("Number of users must be greater than the average"
                             "number of friendships.")

        # Reset graph.
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Load name list.
        with open('first-names.txt') as file:
            names = file.read().split()

        # Add users, assigning a random name to each. (Duplicate names are
        # possible.)
        for i in range(num_users):
            self.add_user(random.choice(names))

        # Create friendships.
        for i in range(num_users * avg_friendships // 2):
            successful = False
            while not successful:
                user1 = random.choice(list(self.users.keys()))
                user2 = random.choice(list(self.users.keys()))
                try:
                    self.add_friendship(user1, user2)
                except ValueError:
                    pass
                else:
                    successful = True

    def get_total_users(self):
        """
        Returns the total number of users in the network.
        """
        return len(self.users)

    def get_total_friendships(self):
        """
        Returns the total number of friendships in the network. (Remember that
        each friendship is listed twice, once in each direction.)
        """
        return sum([len(friend_list) for friend_list in
                    self.friendships.values()]) / 2

    def get_average_friendships(self):
        """
        Returns the mean number of friendships held users in the network.
        """
        num_users = self.get_total_users()
        total_friendships = self.get_total_friendships()
        return 2 * total_friendships / num_users

    def get_min_friendships(self):
        """
        Returns the number of friendships participated in by the user with the
        fewest friends.
        """
        return min([len(friend_list) for friend_list in
                    self.friendships.values()])

    def get_max_friendships(self):
        """
        Returns the number of friendships participated in by the user with the
        most friends.
        """
        return max([len(friend_list) for friend_list in
                    self.friendships.values()])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument.

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        # Use a queue for breadth-first traversal.
        to_visit = SimpleQueue()
        to_visit.put((user_id, None))

        while to_visit.qsize() > 0:
            (vertex, prev) = to_visit.get()

            if vertex not in visited:
                if vertex == user_id:
                    # Self node is always reachable.
                    visited[vertex] = [user_id]
                elif prev == user_id:
                    # Immediate friends are directly reachable from the self.
                    visited[vertex] = [user_id]
                else:
                    # The shortest path to friends of friends is the shortest
                    # path to the previous node through which they are first
                    # reached, plus that previous node.
                    visited[vertex] = visited[prev] + [prev]

            # Add the next outward friends-of-friends circle to the queue for
            # traversal.
            for edge in self.friendships[vertex]:
                if edge not in visited:
                    to_visit.put((edge, vertex))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    print(f'Total Users: {sg.get_total_users()}')
    print(f'Total friendships: {sg.get_total_friendships()}')
    print(f'Average friendships per user: {sg.get_average_friendships()}')
    print(f'Minimum friendships: {sg.get_min_friendships()}')
    print(f'Maximum friendships: {sg.get_max_friendships()}')
    connections = sg.get_all_social_paths(1)
    print(connections)
