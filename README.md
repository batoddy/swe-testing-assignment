# Quick-Calc

Quick-Calc is a simple desktop calculator built with Python and Tkinter. It supports addition, subtraction, multiplication, and division.

This project was developed for a software engineering assignment with a focus on clean structure and testability. The calculation logic and GUI are separated to make the code easier to maintain and test.

## Features

- Four basic arithmetic operations
- Simple Tkinter interface
- Division by zero protection
- Clear button to reset inputs
- Automated tests with `pytest`

## Project Structure

swe-testing-assignment/
├── quick_calc.py
├── tests/
│ ├── test_logic.py
│ └── test_integration.py
├── README.md
└── TESTING.md

## Requirements

- Python 3.10+
- `pytest`

Tkinter is included with most Python installations.

## Installation

```bash
git clone https://github.com/yourusername/swe-testing-assignment.git
cd swe-testing-assignment
pip install pytest
```

### Run the Application

```bash
python quick_calc.py
```

### Run the Tests

```bash
pytest
```

### Version

~v1.0.0~
