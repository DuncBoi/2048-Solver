# 2048 Solver
**Author:** Duncan Greene

This is a 2048 Solver implemented in Python for **COMS 4701 - Artificial Intelligence** at Columbia University

## Setup
- 2048 is played on a 4x4 board in which the user chooses to slide the tiles up, down, left, or right. If two tiles of the same number collide, they merge into a single tile with a value equal to the sum of the two. A demo can be found [here](https://play2048.co/).
- The game is initialized in `GameManager.py` and visualized in the grid class found in `Grid.py`:
  - New tiles spawn randomly in an unoccupied position on the board (90% chance of a 2 tile and 10% chance of a 4 tile)
  - The algorithm is allowed 0.2 seconds to come up with a move

## Algorithm
- My implementation of the solver is found in `IntelligentAgent.py`
- Given a board state, the algorithm uses Iterative Deepening Search with a runtime constraint of under 0.2 seconds per move and a max depth of 3.
- For each depth level, I implemented the Expectiminimax algorithm with alpha-beta pruning 
