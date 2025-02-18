from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Tuple
import asyncio
from trie import Trie

class BookwormSolver:
    __slots__ = ['tries']
    
    def __init__(self):
        self.tries = {}
        
    @lru_cache(maxsize=1024)
    def calculate_word_strength(self, word: str) -> float:
        # Simplified strength calculation - can be enhanced based on actual game rules
        letter_strengths = {
            'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 
            'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
            'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
            'y': 4, 'z': 10
        }
        return sum(letter_strengths.get(c, 0) for c in word.lower())
    
    async def load_dictionary(self, filename: str) -> None:
        trie = Trie()
        path = Path('txt_files') / filename
        with open(path, 'r') as f:
            for line in f:
                word = line.strip()
                if word:
                    trie.insert(word)
        self.tries[filename] = trie
    
    async def load_all_dictionaries(self) -> None:
        tasks = []
        for file in Path('txt_files').glob('*.txt'):
            tasks.append(self.load_dictionary(file.name))
        await asyncio.gather(*tasks)
    
    def find_solutions(self, letters: str) -> Dict[str, List[Tuple[str, float]]]:
        results = {}
        for filename, trie in self.tries.items():
            words = trie.find_words(letters)
            # Get word strengths and sort by strength
            word_strengths = [(word, self.calculate_word_strength(word)) for word in words]
            word_strengths.sort(key=lambda x: (-x[1], x[0]))  # Sort by strength desc, then alphabetically
            results[filename] = word_strengths[:10]  # Only keep top 10
        return results
