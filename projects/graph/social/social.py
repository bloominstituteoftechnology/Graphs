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
    if numUsers < avgFriendships:
      return "Number of users must be greater than avarage number of friendships"

    # Add users
    user_arr = []
    for i in range(0, numUsers - 1):
      self.addUser(i)
      user_arr.append(i + 1)

    # Create friendships
    poss_friendships = []
    for f1 in range(1, len(user_arr)):
      for f2 in range(f1 + 1, len(user_arr)):
        poss_friendships.append([f1, f2])

    # select random friendships until average is filled
    self.fisherYatesShuffle(poss_friendships)
    n = numUsers * avgFriendships // 2
    for i in range(0, n):
      f_id_1 = poss_friendships[i][0]
      f_id_2 = poss_friendships[i][1]
      self.addFriendship(f_id_1, f_id_2)



  def getAllSocialPaths(self, userID):
    """
    Takes a user's userID as an argument

    Returns a dictionary containing every user in that user's
    extended network with the shortest friendship path between them.

    The key is the friend's ID and the value is the path.
    """

    q = []
    visited = {}  # Note that this is a dictionary, not a set
    q.append([userID])
    while len(q) > 0:
      n = q.pop()
      if self.friendships[n[-1]] == set():
        if n[-1] != userID:
          visited[n[-1]] = n
      else:
        for friend in self.friendships[n[-1]]:
          if friend not in visited and friend is not userID:
            path = n + [friend]
            q.append(path)
            visited[path[-1]] = path




    return visited

  def fisherYatesShuffle(self, arr):
    # random.seed(1) # <-- Debugging general pause
    # random.seed(9) # <-- Debugging 1 has no friends
    for i in range(0, len(arr) - 2):
      random_index = random.randint(i, len(arr) - 1)
      arr[random_index], arr[i] = arr[i], arr[random_index]


if __name__ == '__main__':
  sg = SocialGraph()
  sg.populateGraph(10, 2)
  print(sg.friendships)
  connections = sg.getAllSocialPaths(1)
  print(connections)
