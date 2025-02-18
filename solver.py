from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Tuple
import asyncio
import sys
import os
from trie import Trie

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

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
        try:
            # Use resource_path to get the correct path in both dev and exe
            file_path = resource_path(os.path.join('txt_files', filename))
            print(f"Loading dictionary from: {file_path}")  # Debug print
            with open(file_path, 'r') as f:
                for line in f:
                    word = line.strip()
                    if word:
                        trie.insert(word)
            self.tries[filename] = trie
        except Exception as e:
            print(f"Error loading dictionary {filename}: {str(e)}")  # Debug print
            raise
    
    async def load_all_dictionaries(self) -> None:
        try:
            # Get the txt_files directory path
            txt_files_path = resource_path('txt_files')
            print(f"Looking for dictionaries in: {txt_files_path}")  # Debug print
            
            # List all txt files in the directory
            tasks = []
            for file in os.listdir(txt_files_path):
                if file.endswith('.txt'):
                    tasks.append(self.load_dictionary(file))
            
            if not tasks:
                print("No dictionary files found!")  # Debug print
            
            await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Error in load_all_dictionaries: {str(e)}")  # Debug print
            raise
    
    def find_solutions(self, letters: str) -> Dict[str, List[Tuple[str, float]]]:
        results = {}
        for filename, trie in self.tries.items():
            words = trie.find_words(letters)
            # Get word strengths and sort by strength
            word_strengths = [(word, self.calculate_word_strength(word)) for word in words]
            word_strengths.sort(key=lambda x: (-x[1], x[0]))  # Sort by strength desc, then alphabetically
            results[filename] = word_strengths[:10]  # Only keep top 10
        return results
