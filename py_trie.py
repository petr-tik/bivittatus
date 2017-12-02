import string


class TrieNode():

    def __init__(self, letter, is_word=False):
        self.letter = letter
        self.is_word = is_word
        self.children = [None for _ in string.ascii_lowercase]


class PyTrie():

    """
    trie = PyTrie()
    trie.add("bob")
    trie.find("bob")
    True

    """

    def __init__(self):
        self.head = TrieNode("\0", is_word=False)

    @staticmethod
    def char_to_idx(letter):
        return ord(letter) - 97  # ascii for a is 97

    def add(self, new_word):
        """ Add a given word to trie, returns None"""
        cur = self.head

        for char in new_word:
            child = cur.children[PyTrie.char_to_idx(char)]
            if not child:
                new_node = TrieNode(char)
                cur.children[PyTrie.char_to_idx(char)] = new_node
            cur = cur.children[PyTrie.char_to_idx(char)]
        cur.is_word = True
        return None

    def find(self, word):
        """ Returns boolean if word in trie or not """
        cur = self.head
        for char in word:
            child = cur.children[PyTrie.char_to_idx(char)]
            if not child:
                return False
            cur = child

        return cur.is_word == True


def test_trie():
    assert trie.find("bob") == True
    assert trie.find("alice") == False


if __name__ == "__main__":
    test_trie()
