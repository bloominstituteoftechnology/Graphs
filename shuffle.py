import random
def fisher_yates_shuffle(l):
    for i in range(0, len(l) - 2):
        random_index = random.randint(i, len(l) - 1)
        l[random_index] = l[i]
        # swap = l[random_index]
        # l[random_index] = l[i]
        # l[i] = swap

# ```JavaScript
# function shuffle(array) {
#   let m = array.length, t, i;

#   // While there remain elements to shuffle…
#   while (m) {

#     // Pick a remaining element…
#     i = Math.floor(Math.random() * m--);

#     // And swap it with the current element.
#     t = array[m];
#     array[m] = array[i];
#     array[i] = t;
#   }

#   return array;
# }
# ```