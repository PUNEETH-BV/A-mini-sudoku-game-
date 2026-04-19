# Mini Sudoku Game 🧩

A terminal-based 6×6 Sudoku game built from scratch in Python using NumPy and Pandas — no game engine, no shortcuts.

---

## Why I Built This

LinkedIn's daily Sudoku game is addictive. One game a day just wasn't enough. I could have downloaded any app from the Play Store — but where's the fun in that? Instead, I built my own Sudoku engine from scratch using Python, NumPy, and Pandas. Every bug taught me something new.

---

## Features

- Valid 6×6 Sudoku grid — every row, column, and 2×3 box contains 1–6 with no repeats
- Three difficulty levels: Easy (3 blanks), Medium (4 blanks), Hard (5 blanks)
- Interactive terminal gameplay with answer validation
- Live board refresh after every correct answer
- Clean modular code structure — separated into grid generation, display, and game logic

---

## Project Structure

```
mini-sodu-game/
├── grid.py        # Generates a valid 6×6 Sudoku grid using NumPy
├── display.py     # Styles the Pandas DataFrame as a Sudoku table
├── game.py        # Game logic — level selection, blanking, answer validation
├── main.py        # Entry point — runs the game
└── README.md
```

---

## How It Works

### Grid Generation (`grid.py`)
Uses a cyclic Latin square approach with `np.roll` to guarantee no repeats in any row or column:

```python
base = np.random.permutation(np.arange(1, 7))
array = np.array([
    np.roll(base, 0),
    np.roll(base, -2),
    np.roll(base, -4),
    np.roll(base, -1),
    np.roll(base, -3),
    np.roll(base, -5),
])
```

The shift pattern `0, -2, -4, -1, -3, -5` ensures every 2×3 box also satisfies the Sudoku constraint.

### Display (`display.py`)
Wraps a Pandas DataFrame in `.style.set_properties()` to draw thick borders around each 2×3 box — giving it a real Sudoku table feel.

### Game Logic (`game.py`)
- Randomly blanks `n` cells based on difficulty level (no duplicates using `replace=False`)
- Stores `(row, col, value)` tuples for answer validation
- Loops until all blanks are correctly filled

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| NumPy | Grid generation with `np.roll`, `np.random`, `np.block` |
| Pandas | DataFrame display and cell manipulation |
| Jinja2 | Required by Pandas `.style` for HTML rendering |

---

## Installation

```bash
git clone https://github.com/PUNEETH-BV/mini-sodu-game
cd mini-sodu-game
pip install numpy pandas jinja2
python main.py
```

---

## How to Play

```
menu
level 1 : easy
level 2 : medium
level 3 : hard
enter the level : 1

Row : R3 and Col : C2
Row : R5 and Col : C4
Row : R1 and Col : C6

    C1  C2  C3  C4  C5  C6
R1   3   1   5   4   6
R2   5   3   1   6   4   2
R3   1       3   2   5   4
R4   4   5   6   1   2   3
R5   6   4   2       3   1
R6   2   6   4   3   1   5

enter the row : R1
enter the col : C6
enter the guess : 2
correct answer ✓
```

---

## What I Learned

- How `np.block` assembles arrays from smaller pieces
- Why `np.roll` with specific shift patterns creates valid Latin squares
- How Pandas `.style` renders HTML tables with custom borders
- The difference between `df.loc[array_of_rows, array_of_cols]` (intersection) vs iterating pairs (individual cells)
- How to structure a Python project into multiple files with clean imports
- Debugging dtype mismatches between `int64`, `str`, and mixed types in Pandas

---

## Author

**Puneeth B V**
First-year ISE student at SJC Institute of Technology, Bengaluru
[GitHub](https://github.com/PUNEETH-BV) | [LinkedIn](https://www.linkedin.com/in/)
