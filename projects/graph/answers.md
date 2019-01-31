1. To create 100 users with an average of 10 friends each, how many times would you need to call `addFriendship()`? Why?
- You need to call it 500 times. In total you need 1000 friendships, and each call makes two of those. numUsers * avarage // 2

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
- the average connections is between 113 and 125. Found by running the following code a few times...
```
if __name__ == '__main__':
  sg = SocialGraph()
  sg.populateGraph(1000, 5)
  # print(sg.friendships)
  connections = sg.getAllSocialPaths(1)
  print(connections)
  total_keys = 0
  total_extended = 0
  for key, value in connections.items():
    total_keys += 1
    total_extended += len(value)
  print(f'Average connections in extended network: {total_extended/total_keys}')
  ```
  which is between 11 and 12 % of total users