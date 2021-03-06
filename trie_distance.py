from pip._vendor.msgpack.fallback import xrange


class TrieNode:
    """The Trie data structure keeps a set of words, organized with one node
    for each letter. Each node has a branch for each letter that may follow it
    in the set of words."""
    def __init__(self):
        self.word = None
        self.children = {}

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word


def dict_to_trie(name):
    """reads dictionary file into a trie"""
    trie = TrieNode()
    for word in name:
        trie.insert(word)
    return trie


def search(word, max_cost, trie):
    """
    :param word: target word
    :param max_cost: given maximum distance
    :param trie: trie
    :return: a list of all words that are less than the given maximum distance
    """
    # build first row
    current_row = range(len(word) + 1)
    results = []
    # recursively search each branch of the trie
    for letter in trie.children:
        search_recursive(trie.children[letter],
                         letter, word, current_row, results, max_cost)
    return results


def search_recursive(node, letter, word, previous_row, results, max_cost):
    """This recursive helper is used by the search function above.
    It assumes that the previous_row has been filled in already"""
    columns = len(word) + 1
    current_row = [previous_row[0] + 1]

    # Build one row for the letter, with a column for each letter in the target
    # word, plus one for the empty string at column 0
    for column in xrange(1, columns):
        insert_cost = current_row[column - 1] + 1
        delete_cost = previous_row[column] + 1
        if word[column - 1] != letter:
            replace_cost = previous_row[column - 1] + 1
        else:
            replace_cost = previous_row[column - 1]
        current_row.append(min(insert_cost, delete_cost, replace_cost))

    # if the last entry in the row indicates the optimal cost is less than the
    # maximum cost, and there is a word in this trie node, then add it.
    if current_row[-1] <= max_cost and node.word is not None:
        results.append((node.word, current_row[-1]))

    # if any entries in the row are less than the maximum cost, then
    # recursively search each branch of the trie
    if min(current_row) <= max_cost:
        for letter in node.children:
            search_recursive(node.children[letter],
                             letter, word, current_row, results, max_cost)
