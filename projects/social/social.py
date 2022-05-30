import random

class User:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'User({repr(self.name)})'

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):

        if user_id == friend_id:

            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:

            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            
        return True

    def add_user(self, name):

        self.last_id += 1  
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):

            self.reset()

            for i in range(num_users):
                self.add_user(f"User {i}")

            possible_friendships = []
        
            for user_id in self.users:
                for friend_id in range(user_id + 1, self.last_id + 1):
                    possible_friendships.append((user_id, friend_id))
    
            random.shuffle(possible_friendships)
    
            for i in range(num_users * avg_friendships // 2):
                friendships = possible_friendships[i]
                self.add_friendship(friendships[0], friendships[1])
    
    def populate_graph_2(self, num_users, avg_friendships):

            self.reset()

            for i in range(num_users):
                self.add_user(f"User {i}")
    
            target_friendships = num_users * avg_friendships
            total_friendships = 0
    
            collisions = 0
    
            while total_friendships < target_friendships:
                user_id = random.randint(1, self.last_id)
                friend_id = random.randint(1, self.last_id)
    
                if self.add_friendship(user_id, friend_id):
                    total_friendships += 2
                else:
                    collisions += 1
    
            print(f"COLLISIONS: {collisions}")

    def get_all_social_paths(self, user_id):

        visited = {}
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            newuser_id = path[-1]
            if newuser_id not in visited:
                visited[newuser_id] = path
                for friend_id in self.friendships[newuser_id]:
                    if friend_id not in visited:
                            new_path = list(path)
                            new_path.append(friend_id)
                            q.enqueue(new_path)
        return visited

if __name__ == '__main__':
    sogh = SocialGraph()
    sogh.populate_graph(1000, 999)
    print(sogh.users)
    print(sogh.friendships)
    connections = sogh.get_all_social_paths(1)
    print(connections)