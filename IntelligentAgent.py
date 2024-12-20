# Duncan Greene - Columbia University

from BaseAI import BaseAI
import time

class IntelligentAgent(BaseAI):
    def getMove(self, grid):
        #defaults to the first available move
        bestMove = grid.getAvailableMoves()[0][0]
        depth = 1
        startTime = time.process_time()
        #itertive deepening search with timeConstraint taken into effect and max_depth limit of 3 for quicker runtime
        ## Replace the while loop with the following line for quicker runtime (adds a max depth limit):
        #while time.process_time() - startTime < 0.195 and depth <= 3:
        while time.process_time() - startTime < 0.195
            move = self.minimax(grid, depth, float('-inf'), float('inf'), startTime)
            if move is not None:
                bestMove = move
            depth += 1
        return bestMove
    
    def minimax(self, grid, depth, alpha, beta, startTime):
        
        _, move = self.maximize(grid, depth, alpha, beta, startTime)
        return move  
    
    def maximize(self, grid, depth, alpha, beta, startTime):
        #returns -1 if the time has ran out
        currentTime = time.process_time()
        if (currentTime - startTime > 0.195):
            return float('-inf'), None
        
        #returns heuristic for terminal test
        if (depth == 0 or not grid.canMove()):
            return self.heuristic(grid), None
        
        maxVal = float('-inf')
        best = None

        for move, newGrid in grid.getAvailableMoves():
            value = self.minimize(newGrid, depth - 1, alpha, beta, startTime)
            #immediately returns if time limit exceeded
            if value == None:
                #returning -inf signals that time limit has exceeded
                return float('-inf'), None
            if (value > maxVal):
                maxVal = value
                best = move 
            #alpha beta pruning
            alpha = max(alpha, maxVal)
            if (beta <= alpha):
                break   
        return maxVal, best

    def minimize(self, grid, depth, alpha, beta, startTime):
        currentTime = time.process_time()
        if (currentTime - startTime > 0.195):
            return None
        #terminal test
        if (depth == 0 or not grid.canMove()):
            return self.heuristic(grid)
                
        totalValue = 0
        numberOfCells = len(grid.getAvailableCells())
        for cell in grid.getAvailableCells():
            newGrid = grid.clone()
            
            #simulate the choice of tileSize = 2
            newGrid.insertTile(cell, 2)
            value2, _ = self.maximize(newGrid, depth-1, alpha, beta, startTime)
            #immediately returns if time limit exceeded
            if value2 == float('-inf'):
                return None
            #weighted value of tile = 2 given that 90% of new tiles placed have size 2
            weightedValue2 = 0.9 * value2

            #replace the 2 tile with a 4 and simulate again
            newGrid.setCellValue(cell, 4)
            value4, _ = self.maximize(newGrid, depth-1, alpha, beta, startTime)
            #immediately returns if time limit exceeded
            if value4 == float('-inf'):
                return None
            #weighted value of tile = 2 given that 90% of new tiles placed have size 2
            weightedValue4 = 0.1 * value4

            #sum the weighted values
            totalValue += weightedValue2 + weightedValue4
        
        return totalValue / numberOfCells
    
    def heuristic(self, grid):
        #defines a weighted snake pattern that prioritizes tiles to exist in decreasing order, snaking from bottom left to top right
        snake_pattern = [
            [1,  2,  4,  8],
            [128,  64,  32,  16],
            [256,  512,  1024, 2048],
            [32768, 16384, 8192, 4096]
        ]

        snakeScore = 0
        #weights each tile on the grid (exponentially) by how it conforms to the snake pattern listed above
        for x in range(4):
            for y in range(4):
                snakeScore += grid.map[x][y] * snake_pattern[x][y]

        #normalizes snake score in the early stages of 2048 so that emptyTiles plays a bigger factor
        snakeScore = snakeScore/100  
        #provides additional heuristic so that if there is a tie between 2 snake patterns, then the one with more empty tiles will be chose
        empty_cells = len(grid.getAvailableCells())
        
        heuristic_value = snakeScore + empty_cells
        return heuristic_value
    
    
    




            

            
