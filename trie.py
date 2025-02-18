from dataclasses import dataclass
from typing import Dict, Set, List

@dataclass
class TrieNode:
    __slots__ = ['children', 'is_word']
    children: Dict[str, 'TrieNode']
    is_word: bool
    
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    __slots__ = ['root']
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find_words(self, letters: str, min_length: int = 3) -> Set[str]:
        def backtrack(node: TrieNode, path: str, remaining_letters: List[str], words: Set[str]) -> None:
            if node.is_word and len(path) >= min_length:
                words.add(path)
            
            for i, letter in enumerate(remaining_letters):
                if letter in node.children:
                    new_remaining = remaining_letters[:i] + remaining_letters[i+1:]
                    backtrack(node.children[letter], path + letter, new_remaining, words)
        
        words = set()
        letters_list = list(letters.lower())
        backtrack(self.root, "", letters_list, words)
        return words
