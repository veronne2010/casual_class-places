# Casual Class Places
A Python script that randomly assigns seat numbers to students in a classroom with 22 seats arranged in a specific grid layout.

## Description

This tool generates random seat assignments for a classroom of 22 students. Each student receives a unique seat number (1-22) paired with their designated coordinate in the classroom seating chart.

## Seating Layout

The classroom is divided into three sections with a grid-based coordinate system:

### Seat Coordinate Format
```
[student number].[section][row][column]
```

- **Student Number**: Random number from 1 to 22
- **Section**: 
  - `S` = Left side (Sinistra)
  - `C` = Center (Centro)
  - `D` = Right side (Destra)
- **Row** (Horizontal): `x`, `y`, `z`, `a` (front to back)
- **Column** (Vertical): `A` to `G` (left to right within section)

### Seating Arrangement

**Left Section (S)**: 6 seats
- Row x: A, B
- Row y: A, B
- Row z: A, B

**Center Section (C)**: 6 seats
- Row x: C, D
- Row y: C, D
- Row z: C, D

**Right Section (D)**: 10 seats
- Row x: E, F, G
- Row y: E, F, G
- Row z: F, G
- Row a: F, G

**Total**: 22 seats

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `random` module)

## Usage

Run the script from the command line:

```bash
python classroom_randomizer.py
```

## Output Example

```
15.SxA
7.SxB
22.SyA
3.SyB
18.SzA
9.SzB
12.CxC
1.CxD
...
```

Each run generates a new random assignment. Note that numbers may repeat since each coordinate gets an independent random number.

## Use Cases

- Random seating arrangements for exams
- Classroom organization at the start of term
- Fair seat rotation system
- Reducing seating bias or patterns

## License

This project is provided "as-is" without any warranty.
