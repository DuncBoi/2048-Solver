# 2048 Solver
**Author:** Duncan Greene

This is a 2048 Solver implemented in Python for **COMS 4701 - Artificial Intelligence** at Columbia University.

## Setup
- 2048 is played on a 4x4 board in which the user chooses to slide the tiles up, down, left, or right. If two tiles of the same number collide, they merge into a single tile with a value equal to the sum of the two. A demo can be found [here](https://play2048.co/).
- The game is initialized in `GameManager.py` and visualized in the grid class found in `Grid.py`:
  - New tiles spawn randomly in an unoccupied position on the board (90% chance of a 2 tile and 10% chance of a 4 tile).
  - The algorithm is allowed 0.2 seconds to come up with a move.

## Algorithm
- The solver implementation resides in `IntelligentAgent.py`
- The algorithm employs *Iterative Deepening Search* with a runtime constraint of 0.2 seconds per move. The algorithm will choose the move from the deepest search level reached before the time constraint is met.
- At each depth level, the solver employs the *Expectiminimax* algorithm, augmented with &alpha;-&beta; pruning to increase efficiency.

## Heuristic
- Each board state is defined by a numerical heuristic score such that higher values represent more favorable board states
- The heuristic used in this case is largely dependent (90% weight) on this snake matrix:

<div align="center">
<table>
  <tr>
    <td>
      <table>
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
    </td>
    <td style="padding-left: 20px; text-align: center;">
      $$snakeVal = \Large{\sum_{i=1}^{4} \sum_{j=1}^{4}} \tiny{\text{\scriptsize boardState}[i][j] \cdot \text{\scriptsize snake}[i][j]}$$
    </td>
  </tr>
</table>
</div>

- The value of every tile on the board is multiplied by the number in the corresponing position of the snake matrix.
- The board is exponentially weighted to promote monotonicity such that the biggest tile is in the bottom left corner, with subsequent tiles decreasing in a snake-like pattern.
- Also, the number of empty tiles on a given board is factored in to promote open space during early stages of the game and break ties between boards with equal snake heuristic values.
- So: $$Heuristic = 0.9 \cdot snakeVal + 0.1 \cdot emptyTiles$$. (The snake heuristic is scaled down by a factor of 100)
- To account for the randomness of incoming tile placement, the algorithm at min nodes will return the weighted average of the heuristic through all possible new board configurations.
## Usage
1. `python3 GameManager.py`
## Files
- `BaseAI.py`: defines class structure for a player
- `BaseDisplayer.py`: defines class structure for the visualizer
- `ComputerAI.py`: implementation of the computer random move generator
- `Displayer.py`: implementation of the visualizer
- `GameManager.py`: where the game is run
- `Grid.py`: defines how the game board can be manipulated
- `IntelligentAgent.py`: implementation of solver
