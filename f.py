import hashlib
from itertools import permutations

class HashCollisionFinder:
    def __init__(self, anagram):
        self.anagram = anagram
        self.words = self._load_words()

    def _load_words(self):
        with open("words.txt", "r") as word_file:
            return [word.strip() for word in word_file]

    def _filter_words(self, char_list):
        return [word for word in self.words if all(char in char_list for char in set(word))]

    def _hash_string(self, input_str):
        m = hashlib.md5()
        m.update(input_str.encode('utf-8'))
        return m.hexdigest()

    def find_collision(self, original_hash):
        words_count = self.anagram.count(' ') + 1
        char_list = list(set(self.anagram.replace(' ', '')))

        filtered_words = self._filter_words(char_list)
        print(len(filtered_words))

        for elem in permutations(filtered_words, words_count):
            hash_elem = " ".join(elem)

            if len(hash_elem) != len(self.anagram):
                continue

            word_hash = self._hash_string(hash_elem)

            if word_hash == original_hash:
                return hash_elem

# Given hash to find a collision
hash_to_find = 'ac3751fa101668c6de2002356d9a032b'

# Create an instance of the HashCollisionFinder class
collision_finder = HashCollisionFinder(anagram="i move lads")

# Find the collision
collision_word = collision_finder.find_collision(hash_to_find)

# Print the result
print(f"Collision! The word corresponding to the given hash is '{collision_word}'")
