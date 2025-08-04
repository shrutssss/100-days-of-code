# Hangman Game 🎮

A beginner-friendly command-line Hangman game built using Python.  
This project helped me understand how to apply core programming concepts in a fun, interactive way by dividing code into separate files and organizing logic efficiently.

---

## 🔧 Learning Outcome :: What's in the Game 

- Flowchart made using draw.io :: https://drive.google.com/file/d/1DOnB-1GH-I8sOJxAAcZ84nrLGScYHr21/view?usp=sharing
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

## 💡 Concepts I Learned

📦 Python Basics

import statements to use local .py files

random.choice() to select a random word

input() for player guesses

if-else, for, and while loops to manage game logic

🔁 Game Logic

Looping until win/loss condition is met

Tracking correct/incorrect guesses using lists

Managing lives and updating a placeholder word display

📑 Code Organization

Learned how to split code into modules for readability

Used a stages list from hangman_art.py to visualize hangman progress

Displayed a game logo using ASCII art at the start


🙋‍♀️ About Me

I’m Shruti Jahagirdar, a second-year B.Tech CSE (AI & ML) student.
This was one of my first logic-based projects. It helped me learn how to organize code, plan control flow, and use Python in a structured way.
Currently, I’m learning DSA and Python through Striver’s A2Z sheet and the 100 Days of Code challenge.