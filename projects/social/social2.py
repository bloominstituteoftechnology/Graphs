import random

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
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        
        
    def fisheryates(self, arr):
        copy_arr = list(arr)
        #iterate overthe arr
        for idx in range(len(arr)):
        #choose a random index
             rand_index = random.randint(0, len(arr) -1)
        #swap current index with random index   
             copy_arr[idx], copy_arr[rand_index] = copy_arr [rand_index], copy_arr[idx]
        
        return copy_arr     
             
             
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
        for i in range(num_users):
            self.add_user(i)
        
        all_friend_combos = []
        for person in range(1, num_users):
            for friend in range(person +1, num_users+1) :
                all_friend_combos.append( (person, friend))
             
         
        #Shuffle the List
        shuffled_combos = self.fisheryates(all_friend_combos)
        
        total_friendships = num_users * avg_friendships
        
        elements_needed = total_friendships //2
        
        combos_to_make = shuffled_combos[:elements_needed]
        
        #then loop over the list and call add_friendship
        for friendship in combos_to_make:
            self.add_friendship(friendship[0], friendship[1])
        
    def get_neighbors(self, user_id):
        return self.friendships[user_id] 
        
    def search(self,   starting_vertex, destination_vertex, visited= set(), path = []):
        if len(path) == 0:
            path.append(starting_vertex)
            
        if starting_vertex == destination_vertex:
            # path.append(destination_vertex)
            return path
        
        visited.add(starting_vertex)
        
        neighbors = self.get_neighbors(starting_vertex)
        
        if len(neighbors) == 0:
            return None
        
        for n in neighbors:
            if n not in visited:
               new_path = path + [n]
               result = self.search(n, destination_vertex, visited, new_path)
            
               if result is not None:
                  return result
    
    
    def linear_populate_graph(self, num_users, avg_friendships):
        total_friendships_made = 0
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        for i in range(num_users):
            self.add_user(i)
            
            
    #pick 2 random user_ids
        friend_1 = random.randint(1, num_users )
        friend_2 = random.randint(1, num_users)
    #try to make them friends
    ##  track # of friends made        
        freindship_made = self.add_friendship(friend_1, friend_2)
        
        if freindship_made:
            total_friendships_made +=1
           
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q= Queue() 
        
        q.enqueue([user_id])
        
        while q.size()> 0:
            current_path = q.dequeue()
            
            current_user = current_path[-1]
            
            
            if current_user not in visited:
                visited[current_user]= current_path
                
                friends = self.friendships[current_user]
                
                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    q.enqueue(path_copy)
                    
        return visited            
        
             
                   
                
        
        
         
        
         


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000,2)
    print( sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("C",connections)
    
    print(f'Percent of users in extended network {len(connections)/1000 * 100}%')
 