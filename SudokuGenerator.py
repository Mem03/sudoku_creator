class SudokuSolver:
    def __init__(self, size = 9, subgrid_size=3):
        self.size = size
        self.subgrid_size = subgrid_size
        self.grid = [[0] * size for _ in range(size)]
        self.placement_count = 0  # Counter for placements

    # First, print the grid to see what happens
    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))

    def print_puzzle(self):
        for row in self.puzzle:
            print(" ".join(map(str, row)))

    # Finding an empty spot, iterating through grid to find a 0, returning the empty one
    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return i, j
        return None
    
    def is_valid(self, row, col, num):
        # If the number is in the row or column, return false
        for i in range(self.size):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
               
        # Figure out if the number is in the subgrid
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        
        return True  
          
    def create_grid(self):
        empty = self.find_empty()

        if not empty:
            return True

        row, col = empty
        for num in random.sample(range(1, self.size + 1), self.size): #Random sampling to ensure random placement of numbers.
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.create_grid():
                    return True
                self.grid[row][col] = 0
        return False
    
    def generate_full_grid(self):
        self.create_grid()
        return copy.deepcopy(self.grid)  # Return a copy of the full grid

    def is_valid_puzzle(self, row, col, num):
        # If the number is in the row or column, return false
        for i in range(self.size):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False
               
        # Figure out if the number is in the subgrid
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                if self.puzzle[start_row + i][start_col + j] == num:
                    return False
        
        return True  

    def remove_numbers(self, difficulty=10):
        self.puzzle = copy.deepcopy(self.grid)
        number_removed = 0
        while number_removed < difficulty:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.puzzle[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            original = self.puzzle[row][col]
            self.puzzle[row][col] = 0
            solution = 0
            # iterate through numbers
            for i in range(self.size):
                if self.is_valid_puzzle(row, col, i):
                    solution += 1
            if solution == 1:
                number_removed += 1     
            else:
                self.puzzle[row][col] = original