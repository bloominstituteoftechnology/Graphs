from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.reset()

    def reset(self):
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
        self.reset()
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i}')

        # Create friendships
        import random
        all_friendships = []
        for i in range(num_users - 1):
            for j in range(i+1, num_users):
                all_friendships.append([i+1,j+1]) 
        
        random.shuffle(all_friendships)
        
        for i in range(num_users * avg_friendships // 2):
            self.add_friendship(all_friendships[i][0], all_friendships[i][1])


    def get_all_social_paths(self, user_id, visited=None):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if visited == None:
            visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        if user_id not in visited:
            visited[user_id] = [user_id]
        else:
            visited[user_id] = visited[user_id] + [user_id]
        
        q = Queue()
        for friend in self.friendships[user_id]:
            if friend not in visited:
                q.enqueue(friend)
                visited[friend] = visited[user_id]
        
        while q.size() > 0:
            id = q.dequeue()
            # print('calling for', friend, 'with', visited)
            self.get_all_social_paths(id, visited)

        # print('returning for', user_id, 'with', visited)
        return visited
        


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)