import random

def populate_graph(self, num_users, avg_friendships):
    # Reset graph
    self.last_id = 0
    self.users = {}
    self.friendships = {}

    # Add users
    for i in range(0, num_users):
        self.addUser(f"User {i}")

    # Create Frienships
    # Generate all possible friendship combinations
    possible_friendships = []

    # Avoid duplicates by ensuring the first number is smaller than the second
    for user_id in self.users:
        for friend_id in range(user_id + 1, self.last_id + 1):
            possible_friendships.append((user_id, friend_id))

    # Shuffle the possible friendships
    random.shuffle(possible_friendships)

    # Create friendships for the first X pairs of the list
    # X is determined by the formula: num_users * avg_friendships // 2
    # Need to divide by 2 since each add_friendship() creates 2 friendships
    for i in range(num_users * avg_friendships // 2):
        friendship = possible_friendships[i]
        self.add_friendship(friendship[0], friendship[1])
