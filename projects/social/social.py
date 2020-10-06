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
        if user_id == friend_id:
            pass
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            pass
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):        
        import random
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
 
        for e in range(num_users):
            self.add_user(e)

        for user in range(1, len(self.users) + 1):
            for _ in range(random.randrange( avg_friendships * 2)):
                self.add_friendship(user, random.randrange(user)+1)
                
    def get_all_social_paths(self, user_id):
        visited = set()  

        queue = Queue()
        queue.enqueue([user_id])        

        while queue.size() > 0:
            path = queue.dequeue()

            node = path[-1]

            if node not in visited:
                neighbours = self.friendships[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour) 
                    queue.enqueue(new_path)
                    print("new", new_path)

                visited.add(node)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
