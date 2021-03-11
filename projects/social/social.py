import string
import random


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
        names = list(string.ascii_uppercase)
        for i in range(num_users):
            self.add_user(names[i])

        # Create friendships
        for user in self.users:
            potential_friends = list(range(1, num_users + 1))
            potential_friends.remove(user)
            random.shuffle(potential_friends)
            # Need to modify the randomization of length
            length = random.randint(0, 2)
            for n in potential_friends[0:length+1]:
                if user < n:
                    self.add_friendship(user, n)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create an empty queue
        # enqueue the first path.
        # while the q is not empty.
        # dequeue the path.
        # set a newuser_id to the last element in the path [-1]
        # if the newuser_id is not in visited.
        # set the visited at the key of newuser_id to the path.
        # for every friend_id in the friendships at the key of newuser_id
        # make a copy of the path called new_path.
        # append the friend_id to the new_path.
        # enqueue the new path.
        # return the populated visited dict to the caller
        q = []
        q.append(user_id)
        length = len(self.friendships[user_id]) + 1
        # counter = 1

        prevPath = set([user_id])

        # TODO should remove checking the length. it's here to keep the loop short
        while len(q) > 0 and length > 0:
            print("----")
            current = q.pop(0)
            # print(prevPath)
            # if current == user_id:
            #     print(list(self.friendships[current]))
            #     q.append(list(self.friendships[current]))
            # else:
            for i in self.friendships[current]:
                print(i)
                print(prevPath)
                if i in visited:
                    prevPath = prevPath.union(visited[i])
                    # print(visited[i])
                else:
                    prevPath.add(i)
                    q.append(i)

            if current not in visited:
                visited[current] = prevPath
            # else:
                # combine paths of the prev nodes
            # counter = counter + 1
            length = length - 1

        return visited


# if __name__ == '__main__':
sg = SocialGraph()
sg.populate_graph(10, 2)
print(sg.friendships)
connections = sg.get_all_social_paths(1)
print(connections)
