# MathFinder

MathFinder is a project designed to discover mathematical expressions and approximate numeric values using fundamental mathematical operations and search algorithms. The project aims to expand toward approximating irrational and transcendental numbers.

## Features & Search Algorithms Implemented

- **Iterative Deepening Depth-First Search (`iterative_dfs`)**: Explores mathematical operation trees up to a configurable depth limit without getting stuck in infinite paths.
- **Breadth-First Search (`dobfs`)**: Explores mathematical operation trees level by level to find the shortest expression sequence.
- **Beam Search (`dobeam`)**: Employs a priority queue (min-heap) ordered by target distance to restrict search width at each depth, enabling fast search over large search spaces.

## Mathematical Operations Supported

- Arithmetic: `+`, `-`, `*`, `/`
- Transcendental & Exponential: $e^x$, $\log(x)$
- Trigonometric: $\sin(x)$, $\cos(x)$, $\tan(x)$
- Roots: $\sqrt{x}$

## Usage

Run `main.py` with a target value and layer/width argument:

```bash
python main.py <target_value> <layers_or_width>
```

### Examples

```bash
python main.py 50 3
python main.py 201 30
```
