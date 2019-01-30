from itertools import combinations
import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        for user in range(1, numUsers + 1):
            self.addUser(user)

        half = int((numUsers * avgFriendships) / 2)
        possible_friendships = list(combinations(range(1, len(self.users) + 1), 2))
        random.shuffle(possible_friendships)
        actual_friendships = possible_friendships[:half]
        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])


    def getAllSocialPaths(self, userID):
        visited = {}  # Note that this is a dictionary, not a set

        for user in self.users:
            to_visit = []
            friends_searched = set()
            to_visit.append([userID])

            while len(to_visit) > 0:
                deq_path = to_visit.pop(0)
                deq_user = deq_path[-1]
                if deq_user not in friends_searched:
                    if deq_user == user:
                        visited[user] = deq_path
                        break

                    friends_searched.add(deq_user)

                    for friend in self.friendships[deq_user]:
                        copied_path = list(deq_path)
                        copied_path.append(friend)
                        to_visit.append(copied_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
