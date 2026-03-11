# Word Guess Game (Hangman)

A simple terminal-based Hangman game written in Python.

## Requirements

- Python 3.10+ (tested with Python 3.14)
- pytest (for tests)

Install pytest if needed:

```bash
python3 -m pip install pytest
```

## Run the Game

From the project root:

```bash
python3 main.py
```

## Run the Tests

Run all tests:

```bash
python3 -m pytest test_main.py -v
```

## Project Files

- `main.py`: Game logic and game loop
- `test_main.py`: Unit tests for `update_game_state`
