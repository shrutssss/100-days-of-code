# Hangman Game 🎮

A beginner-friendly command-line Hangman game built using Python.  
This project helped me understand how to apply core programming concepts in a fun, interactive way by dividing code into separate files and organizing logic efficiently.

---

## 🔧 Learning Outcome :: What's in the Game 

- random python library :: The computer picks a random word from a predefined list.
- Loops :: The player guesses one letter at a time. Incorrect guesses reduce lives — represented visually as a hangman figure.
- The game ends when the player either guesses all letters or runs out of lives.

---

## 📂 Project Structure

This project uses **modular Python files** to keep code clean and reusable:

- `Hangman.py`: Main game logic
- `hangman_words.py`: Contains the list of possible words (`word_list`)
- `hangman_art.py`: Stores ASCII art for the hangman figure and game logo

We import these using:

```python
import random
import hangman_words
import hangman_art
