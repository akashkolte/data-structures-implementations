# TODO

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        pass
    
    def search(self, word):
        pass
    
    def delete(self, word):
        pass
    
    def has_prefix(self, prefix):
        pass
    
    def starts_with(self, prefix):
        pass
    
    def list_words(self):
        pass
    
    def autocomplete(self, prefix):
        pass

if __name__ == "__main__":
    trie = Trie()

    trie.insert('hello')
    trie.insert('henry')
    trie.insert('mike')
    trie.insert('minimal')
    trie.insert('minimum')
    trie.insert('akash')

    print(trie.list_words())
    print(trie.has_prefix('mi'))
    print(trie.starts_with('mi'))
    trie.delete('minimal')
    print(trie.starts_with('mi'))

    print(trie.search('minimum'))
    print(trie.search('minimal'))
    print(trie.search('mini'))

    trie.insert('mini')
    print(trie.starts_with('mi'))