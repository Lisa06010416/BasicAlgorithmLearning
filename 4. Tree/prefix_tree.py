from typing import List


class Node:
    def __init__(self, val=None, next=None, is_end=False):
        self.val = val
        self.next = next if next else {}
        self.is_end = is_end


"""211. Design Add and Search Words Data Structure"""
class WordDictionary:
    """見一個WordDictionary物件可以提供提加入字以及查詢加入的字的功能，查詢時會有.代表比對任何letter
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.search(".ad"); // return True
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.prefix_tree = Node()

    def addWord(self, word: str) -> None:
        head = self.prefix_tree
        for letter in word:
            if letter not in head.next:
                head.next[letter] = Node(val=letter)
            head = head.next[letter]
        head.is_end = True

    def _dfs_search(self, root, word):
        if not word and root.is_end:
            return True
        if not word:
            return False

        target = word[0]
        has_match = False
        if target == ".":
            for ner in root.next:
                has_match = self._dfs_search(root.next[ner], word[1:])
                if has_match:
                    break
        else:
            if target in root.next:
                has_match = self._dfs_search(root.next[target], word[1:])

        return has_match

    def search(self, word: str) -> bool:
        return self._dfs_search(self.prefix_tree, word)


"""208. Implement Trie (Prefix Tree)"""
class TreeNode:
    def __init__(self, val="", is_word=False, next=None):
        self.val = val
        self.is_word = is_word
        self.next = {} if not next else next


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp_root = self.root
        if not word:
            return
        for cha in word:
            if cha not in temp_root.next:
                temp_root.next[cha] = TreeNode(val=cha)
            temp_root = temp_root.next[cha]
        temp_root.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp_root = self.root
        for cha in word:
            if cha not in temp_root.next:
                return False
            temp_root = temp_root.next[cha]
        if temp_root.is_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp_root = self.root
        for cha in prefix:
            if cha not in temp_root.next:
                return False
            temp_root = temp_root.next[cha]
        return True


"""212. Word Search II"""
class Solution:
    """ 給予一個字母board,跟一串word,回傳有哪些word在board中
    prefix tree + backtracking
    """
    def _dfs(self, board, i, j, root, word):
        if (i < 0 or j < 0) or (i >= len(board) or j >= len(board[0])):
            return
        if board[i][j] == "@":
            return

        temp_char = board[i][j]
        board[i][j] = "@"

        if temp_char in root:
            if "#" in root[temp_char]:
                self.answer[word + temp_char] = None
            for next_i, next_j in [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1)]:
                self._dfs(board, next_i, next_j, root[temp_char], word + temp_char)
        board[i][j] = temp_char

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # prefix tree
        self.root = {}
        for w in words:
            w = w + "#"
            temp_root = self.root
            for c in w:
                if c not in temp_root:
                    temp_root[c] = {}
                temp_root = temp_root[c]

        # backtracking
        self.answer = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._dfs(board, i, j, self.root, "")
        return self.answer.keys()
