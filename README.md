# 2048 Solver
**Author:** Duncan Greene

This is a 2048 Solver implemented in Python for **COMS 4701 - Artificial Intelligence** at Columbia University

## Setup
- 2048 is played on a 4x4 board in which the user chooses to slide the tiles up, down, left, or right. If two tiles of the same number collide, they merge into a single tile with a value equal to the sum of the two. A demo can be found [here](https://play2048.co/).
- The game is initialized in `GameManager.py` and visualized in the grid class found in `Grid.py`:
  - New tiles spawn randomly in an unoccupied position on the board (90% chance of a 2 tile and 10% chance of a 4 tile)
  - The algorithm is allowed 0.2 seconds to come up with a move

## Algorithm
- The solver implementation resides in `IntelligentAgent.py`
- The algorithm employs *Iterative Deepening Search* with a runtime constraint of 0.2 seconds per move. The algorithm will choose the move from the deepest search level reached before the time constraint is met.
- At each depth level, the solver employs the *Expectiminimax* algorithm, augmented with &alpha;-&beta; pruning to increase efficiency.

## Heuristic
- Each board state is defined by a numerical heuristic score such that higher values represent more favorable board states
- The heuristic used in this case is largely dependent (90% weight) on this snake matrix:

<style>
  .centered-table {
    width: 80%;
    margin: 0 auto;
    border-collapse: collapse;
  }
  .centered-table td {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
    font-family: Arial, sans-serif;
  }
  sup {
    font-size: 0.8em;
    color: #555;
  }
</style>

<table class="centered-table">
  <tr>
    <td>2<sup>0</sup></td>
    <td>2<sup>1</sup></td>
    <td>2<sup>2</sup></td>
    <td>2<sup>3</sup></td>
  </tr>
  <tr>
    <td>2<sup>7</sup></td>
    <td>2<sup>6</sup></td>
    <td>2<sup>5</sup></td>
    <td>2<sup>4</sup></td>
  </tr>
  <tr>
    <td>2<sup>8</sup></td>
    <td>2<sup>9</sup></td>
    <td>2<sup>10</sup></td>
    <td>2<sup>11</sup></td>
  </tr>
  <tr>
    <td>2<sup>15</sup></td>
    <td>2<sup>14</sup></td>
    <td>2<sup>13</sup></td>
    <td>2<sup>12</sup></td>
  </tr>
</table>

- 
