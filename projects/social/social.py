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

        # Add users
        for i in range(num_users):
            self.add_user(i + 1)

        # Create friendships
        num_friends = {} # number of friends each person will have
        for i in range(1, num_users + 1):
            # add number of friends equal to num between .5n to 1.5n
            # where n is average friendships
            # normally distributed
            n = round(random.normalvariate(avg_friendships, avg_friendships * 0.5))
            num_friends[i] = n
        
        # friendship creation loop
        # print(f'User list: {[x for x in self.users]}')
        for i in range(1, num_users + 1):
            n = num_friends[i]
            # get list of everyone
            other_people = list(range(1, num_users + 1))
            # remove yourself
            other_people.remove(i)
            # remove anyone who's already got enough friends
            r = []
            for person in other_people:
                if num_friends[person] <= 0:
                    r.append(person)
            for person in r:
                other_people.remove(person)
            # check if other_people is empty
            if not other_people:
                num_friends[i] = 0
                n = 0
            # add friendships
            # print(f'Person {i} adding friends from {other_people}')
            # print(f'Friends left in each: {[num_friends[n] for n in other_people]}')
            while n > 0:
                other_person = random.choice(other_people)
                self.add_friendship(i, other_person)
                n -= 1
                num_friends[i] -= 1
                num_friends[other_person] -= 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = []
        queue.append(user_id)
        while len(queue) > 0:
            cur_user = queue.pop(0)
            print(cur_user, queue)
            # get all connections
            for friend in self.friendships[cur_user]:
                # don't add people we're already looking to add
                # or that we've already added
                if friend not in queue and friend not in visited:
                    queue.append(friend)
            
            # create links backward
            # first visited catch
            if cur_user == user_id:
                visited[cur_user] = [cur_user]
            else:
                # this should only run once
                for conn in [x for x in self.friendships[cur_user] if x in visited]:
                    visited[cur_user] = visited[conn][:] # copy connection
                    visited[cur_user].append(cur_user) # add current node

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
