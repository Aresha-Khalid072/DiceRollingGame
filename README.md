# Dice Rolling Game

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Type](https://img.shields.io/badge/Interface-Command%20Line-lightgrey)

A command-line application written in Python that simulates rolling a pair of dice. Developed as **Task 1** of the Python Development internship at **Arch Technologies**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation and Usage](#installation-and-usage)
- [Sample Output](#sample-output)
- [Code Structure](#code-structure)
- [Input Validation](#input-validation)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## Overview

Each time a roll is made, the program generates two random integers between 1 and 6 (inclusive), one for each die. It displays the individual results and their total, then asks the user whether to roll again. The game continues until the user chooses to stop.

## Features

- Simulates a pair of six-sided dice using Python's `random` module
- Displays the value of each die and the combined total
- Prompts the user to roll again after every roll
- Accepts `yes`, `y`, `no` or `n`, regardless of letter case or surrounding spaces
- Rejects invalid input and repeats the prompt without crashing
- Reports the total number of rolls when the game ends

## Requirements

| Requirement | Details |
|-------------|---------|
| Python      | Version 3.6 or higher (uses f-strings) |
| Libraries   | None. Only the built-in `random` module is used |

## Installation and Usage

1. Download or clone the repository:

   ```bash
   git clone https://github.com/Aresha-Khalid072/DiceRollingGame.git
   cd DiceRollingGame
   ```

2. Run the program:

   ```bash
   python dice_rolling_game.py
   ```

   On some systems, use `python3` instead of `python`.

## Sample Output

```
====================================
       DICE ROLLING GAME
====================================

Roll #1
  Die 1: 1
  Die 2: 3
  Total: 4

Roll again? (yes/no): yes

Roll #2
  Die 1: 5
  Die 2: 5
  Total: 10

Roll again? (yes/no): maybe
Invalid input. Please type 'yes' or 'no'.

Roll again? (yes/no): no

Thanks for playing! You rolled 2 time(s).
```

Dice values are random, so results differ on every run.

## Code Structure

```
DiceRollingGame/
├── dice_rolling_game.py    # Main program
└── README.md               # Project documentation
```

| Component | Description |
|-----------|-------------|
| `roll_dice()` | Returns two random integers from 1 to 6 using `random.randint(1, 6)` |
| `main()` | Controls the game flow: rolling, displaying results and prompting the user |
| Outer `while` loop | Repeats the game until the user chooses to stop |
| Inner `while` loop | Repeats the prompt until a valid answer is entered |
| `if __name__ == "__main__"` | Ensures the game runs only when the file is executed directly |

## Input Validation

User input is cleaned with `.strip().lower()` and checked against the accepted values (`yes`, `y`, `no`, `n`). Any other input displays an error message and the question is asked again.

## Testing

The program was tested manually with the following cases:

| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Roll again | `yes` / `y` | Dice are rolled again | Passed |
| Stop playing | `no` / `n` | Game ends and shows the roll count | Passed |
| Invalid answer | `maybe` | Error message, prompt repeated | Passed |
| Letter case and spaces | `YES`, ` No ` | Accepted correctly | Passed |
| Dice range | Any roll | Each die is between 1 and 6 | Passed |

## Future Enhancements

- ASCII art display of the dice faces
- "Doubles" detection with a special message
- Roll history and average total at the end of a session

## Author

**Aresha Khalid**
Python Development Intern, Arch Technologies
Email: areshakhalid072@gmail.com

---

*Developed as part of the Arch Technologies internship program.*