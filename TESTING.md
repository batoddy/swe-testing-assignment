# TESTING.md

## Overview

This project includes two types of tests:

- **Unit tests** for the `Calculator` class
- **Integration tests** for the `CalculatorGUI` class

The goal is to test both the arithmetic logic and the basic interaction between the GUI and the logic.

## What Is Tested

### Unit Tests

The unit tests check:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero
- Negative numbers
- Decimal numbers
- Very large numbers

These tests verify that the core calculator logic works correctly.

### Integration Tests

The integration tests simulate basic user actions in the interface:

- Entering two values and clicking an operation button
- Performing a calculation and then pressing **Clear**

These tests confirm that the GUI connects correctly to the calculation logic.

## What Is Not Tested

The following are outside the current scope:

- Visual design and styling
- Theme behavior
- Popup dialog appearance
- Performance and memory usage

The focus of this assignment is functional correctness.

## Relation to Testing Concepts

### Testing Pyramid

Most tests are **unit tests**, and a smaller number are **integration tests**. This follows the testing pyramid approach, where fast and focused tests form the base.

### Black-box and White-box Testing

- **Unit tests** are closer to **white-box testing** because they directly test known methods.
- **Integration tests** are closer to **black-box testing** because they check user-visible behavior.

### Functional Testing

This project mainly uses **functional testing**. The tests verify that calculations are correct, errors are handled properly, and the clear function works as expected.

### Regression Testing

These tests also support **regression testing**. If the code changes later, running the test suite helps confirm that existing features still work.

## Run the Tests

```bash
pytest
```
