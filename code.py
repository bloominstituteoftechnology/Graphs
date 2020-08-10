# Print out all of the strings in the following array in alphabetical order, each on a separate line.

string = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'

# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# ------------------------------- STRETCH -------------------------------
# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.

# function to use as the key for sorting
def middle(s):
    # find the middle letter of the string
    middle = len(s) // 2

    # find the letter at the index of middle
    letter = s[middle]

    return letter.lower()

# function to sort the array
def sort_alphabetical(S):
    # S.sort()
    S.sort(key=middle)

    # iterate through the list of strings
    for i in S:
        print(i)

sort_alphabetical(string)