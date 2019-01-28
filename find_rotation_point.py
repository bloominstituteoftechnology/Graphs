def find_rotation_point(words):
  first_word = words[0]
  floor_index = 0
  ceiling_index = len(words) - 1
  
  while floor_index < ceiling_index:
    # guess a point halfway between floor and ceiling
    guess_index = (ceiling_index + floor_index) // 2
    # if the guess comes after the first word or is the first word
    if words[guess_index] >= first_word:
      # go right
      floor_index = guess_index
    else:
      # go left
      ceiling_index = guess_index
    
    # check if floor and ceiling indices have converged
    if floor_index + 1 == ceiling_index:
      break
  
  return ceiling_index

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

# Write a function that, given a list of words such as this, returns the index of the rotation point. You can assume that no words will be duplicated.

print(find_rotation_point(words))  # returns 5