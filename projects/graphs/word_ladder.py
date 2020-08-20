# Import libraries, packages, modules, classes/functions:
from graph_bidirectional import Graph
from data_structures import Queue, Stack


# Fixed variables (constants):
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class WordLadder(Graph):
    """
    Creates a word ladder for the provided start_word and end_word, with methods that find the 
    shortest path between the two.
    """
    def __init__(self, start_word:str, end_word:str, filename):
        # Initialize from Graph class:
        super().__init__()

        # Convert input arguments start_word and end_word to all lowercase, to make sure all chars are lowercase:
        start_word = start_word.lower()
        end_word = end_word.lower()

        # Read words from file into set words_list:
        with open(filename, 'r') as file:
            self.words_list = set(file.read().split("\n"))  # Set (hash table) enables faster lookup later

        # Add vertex for start word to our word ladder (graph):
        self.add_vertex(start_word)

        # Build word ladder (graph) from start_word to end_word:
        self.build_ladder(words_to_process={start_word}, end_word=end_word)

        # Get shortest path from start_word to end_word using bread-first search (BFS):
        self.path = self.get_path(start_word=start_word, end_word=end_word)
    
    def build_ladder(self, words_to_process:set, end_word):
        """
        Builds a word ladder (graph) from the input set of words_to_process to the end_word, 
        such that neighboring vertices in the graph are only 1 letter different from each other.
        """
        # Base case #1: No possible one-letter-away words left to add:
        if len(words_to_process) < 1:
            return
        
        # List of words 1-degree away from the current words (in words_to_process):
        words_one_letter_away = set()

        # Get neighboring words (1 letter different) for each word in words_to_process, 
        # and add those neighboring words to the word ladder (graph).
        for word in words_to_process:
            # Get list of all 1-away (one letter changed) variants of the word:
            self.get_one_letter_variants(word=word)

            # Base case #2: If current word is end_word, return PATH:
            if end_word in self.vertices[word]:
                return
            
            # If end_word is not among current word's neighboring words, then add those neighboring 
            # words to the list to process in the next (recursive) run-through in the return below:
            for neighbor in self.vertices[word]:
                words_one_letter_away.add(neighbor)
        
        # Recurse toward above base cases by running same method with next "level" of words 
        # (neighboring words 1 letter away from words in words_to_process):
        return self.build_ladder(words_to_process=words_one_letter_away, end_word=end_word)
    
    def get_one_letter_variants(self, word):
        """
        Get list of all 1-away (one letter changed) variants of the word, and add them 
        as vertices in our word ladder (graph), with edges connecting them to word.
        """
        # Make sure word is in the word ladder's existing vertices:
        if word not in self.vertices:
            raise IndexError(f"word {word} is not in this word ladder.")
        
        # Find all valid variants of word (valid: in our words_list), and add as connected vertices 
        # in our word ladder (graph):
        for letter_num in range(len(word)):
            for letter in ALPHABET:
                new_word = word[0:letter_num] + letter + word[letter_num+1:]
                if new_word in self.words_list and new_word != word:
                    if new_word not in self.vertices:
                        self.add_vertex(new_word)
                    self.add_edge(v1=word, v2=new_word)
    
    def get_path(self, start_word, end_word):
        """
        Run a breadth-first search (BFS) to find a shortest path from start_word to end_word.
        """
        return self.bfs(starting_vertex=start_word, target_vertex=end_word)


# -----------------------------------------------------------------------------------
# Test:
start_word = "funny"  # "hungry" "trapeze" "orangutan"
end_word = "lucky"
wl = WordLadder(start_word=start_word, end_word=end_word, filename="words.txt")
print(wl.path)
