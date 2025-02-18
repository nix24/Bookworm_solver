# Bookworm Solver

An efficient solver for the Bookworm puzzle game, leveraging Python, UV for dependency management, and NiceGUI for a modern interface.

## Key Features

- Fast word lookup using a Trie data structure
- Customizable dictionary loading from multiple text files
- Scoring system based on letter weights
- Clean, responsive UI built with NiceGUI

## Technical Stack

- **Language:** Python
- **Dependency Management:** UV
- **UI Framework:** NiceGUI
- **Core Data Structure:** Optimized Trie for word storage and retrieval

## Performance Optimizations

- Asynchronous operations for responsive UI
- Trie serialization for faster startup
- Profiling and targeted optimizations in critical code paths

## Usage

1. Clone the repository

Using UV:
2. Install dependencies (uv installs automatically when running): `uv venv`
3. Run the application: `uv run python main.py`

Using pip:
2. Install dependencies: `pip install .`
3. Run the application: `python main.py`

## Roadmap

1. Trie implementation and testing
2. Dictionary loading functionality
3. Scoring algorithm development
4. UI integration with NiceGUI
5. Performance optimization
6. Comprehensive testing

## Future Enhancements

- Advanced solver algorithms
- Interactive puzzle input
- Difficulty levels

## Letter Weights

| Weight | Letters |
|--------|---------|
| 1      | A, D, E, G, I, L, N, O, R, S, T, U |
| 1.25   | B, C, F, H, M, P |
| 1.5    | V, W, Y |
| 1.75   | J, K, Q |
| 2      | X, Z |
| 2.75   | Qu (special case) |

For detailed scoring information and game mechanics, please refer to the documentation.