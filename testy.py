# SPRINT
# Overall goal is to generate a path that if traveres will go to every node at least once

# DFT - Go in one direction until you get stuck.

# BFS - when your stuck and find an empty room (no exits)

# H - When stuck and want to do BFS to find empty  room, recomends doing bft without moving player
# in order to just do bft on all the rooms. It will return a path walk your player down that path. (BACKTRACK)



#                                        #
#                002                     #
#                 |                      #
#                 |                      #
#                001                     #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #


""" 
Problem needing to be solved. 

- Repeating paths I need for my player to be able to go down a path and then when they reach the end go back. 

- so using the random path thing isn't going to work. 

- I need to make it so when the player get's back to the 0 for example he is able to already eliminate paths that he already went down.

- check for ? marks and queue up those somehow.