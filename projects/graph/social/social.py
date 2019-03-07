import random
from itertools import combinations


class User:
    def __init__(self, name):
        self.name = name #Vertex

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {} #edges

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

    def breadth_first_search(self, starting_vertex, target):
        # create a _queue_ FIFO
        q = []
        visited = []
        # Enqueue the starting vertex
        q.append(starting_vertex)
        print("Queue: ",q)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue a node from the queue
            path = q.pop()
            # print(type(path))
            if type(path) == int:
                node = path
            else:
                node = path[-1]
            if node not in visited:
                # Mark it as visited
                visited.append(node)
                # print("visited breadth search: ",visited)
                if target in visited:
                    print("Path: ",path)
                    print("Dup_Path: ", dup_path)
                    return dup_path
                # Enqueue all of its children
                for i in self.friendships[int(node)]:
                    if i not in visited:
                        if type(path) == int:
                            dup_path = [path]
                        else:
                            dup_path = list(path)
                        dup_path.append(i)
                        q.append(dup_path)

        return None

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        social_g = SocialGraph()
        for i in range(numUsers):
            social_g.addUser(f"Username: {i}")

        possible_friendships = list(combinations(range(1, len(social_g.users) + 1), 2))
        random.shuffle(possible_friendships)
        total = (numUsers*avgFriendships)//2
        print("Theoretical Friendships: ",len(possible_friendships))
        print("Total Actual Friendships: ",total)
        percent_others = (total/len(possible_friendships))*100
        print(f"Percentage of extended network: {percent_others}%", )
        print(f"")
        actual_friendships = possible_friendships[:total]
        for friendship in actual_friendships:
            social_g.addFriendship(friendship[0], friendship[1])
        self.friendships = social_g.friendships


        # Add users

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # sg = SocialGraph()
        print("inside getAllSocialPaths", self.friendships )
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for i in self.friendships[userID]:
            visited[i] = sg.breadth_first_search(userID, i)
        count = 0
        for connections in visited:
            list_conn = []
            list_conn.append(connections)
            print("listed connections for average: ", visited[connections])
            print("connections degree length: ", len(visited[connections]) - 1)
            degrees = len(visited[connections])-1
            count+=degrees
            print("connections in xxxxxxx", connections)


        print("Average Degree of separation: ", count/len(visited))
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populateGraph(10, 3)
    # print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
    # sg.populateGraph(100, 10)
    sg.populateGraph(100, 5)
    print(sg.friendships)
    print("connections: ",sg.getAllSocialPaths(1))
