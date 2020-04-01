def print_board(board):
    '''
    Function to visualize a given Sudoku board
    
    INPUT:
        board <- list of lists (should be 9 x 9 but input does not have to be)
        
    OUTPUT:
        strings
    '''
    
    # string for horizontal lines shown in Sudoku board
    line = '- ' * 13
    
    for row_ind in range(len(board)):
        # horizontal lines
        if row_ind % 3 == 0:
            print(line)
            
        for col_ind in range(len(board[0])):
            # vertical lines
            if col_ind % 3 == 0:
                print('| ', end = '')
            
            # numbers in Sudoku
            print(str(board[row_ind][col_ind]) + ' ', end = '')
            
            # right most vertical lines
            if col_ind == 8:
                print('|')
        
        # bottom most horizontal last
        if row_ind == 8:
            print(line)


def first_empty(board):
    '''
    Function to find the index of the first empty box in a Sudoku board 
    scanning through the elements row by row
    
    INPUT:
        board <- list of lists (should be 9 x 9 but input does not have to be)
    
    OUTPUT:
        index of first empty element as a tuple if there is an empty element
        False if the board is filled
    '''
    
    # row index counter
    row_ind = 0
    
    for row in board:
        # column index counter
        col_ind = 0
        
        for value in row:
            # if empty return index as a tuple
            if value == 0:
                return (row_ind, col_ind)
            
            # increase column index
            col_ind += 1
            
        # increase row index 
        row_ind += 1
    
    # if board not empty return False
    return False


def is_num_allowed(board, num, ind):
    '''
    Function to check if element satisfies Sudoku rules
    
    INPUT:
        board <- list of lists (should be 9 x 9 but input does not have to be)
        num <- int of a value to be tested
        ind <- tuple of index to be tested
    
    OUTPUT:
        True if the value and position satisfies Sudoku rules
    '''
    
    # index
    row = ind[0]
    col = ind[1]
    
    # checking if same number appears in row
    for col_ind in range(len(board[0])):
        if board[row][col_ind] == num and col_ind != col:
            return False
    
    # checking if same number appears in column
    for row_ind in range(len(board)):
        if board[row_ind][col] == num and row_ind != row:
            return False
        
    # checking if same number appears in box
    row_lower = (row // 3) * 3
    row_upper = row_lower + 3
    col_lower = (col // 3) * 3
    col_upper = col_lower + 3
    
    for row_ind in range(row_lower, row_upper):
        for col_ind in range(col_lower, col_upper):
            if board[row_ind][col_ind] == num and (row_ind, col_ind) != ind:
                return False
    
    # Sudoku conditions are satisfied
    return True


def solve_board(board):
    '''
    Function to solve a Sudoku board
    
    INPUT:
        board <- list of lists (should be 9 x 9 but does not have to be)
        
    OUTPUT:
        True if solved
    '''
    
    empty_index = first_empty(board)
    
    # if there are no empty elements, board is solved
    if empty_index:
        row_ind, col_ind = empty_index
    else:
        return True
    
    for value in range(1, 10):
        # first value filled
        if is_num_allowed(board, value, (row_ind, col_ind)):
            board[row_ind][col_ind] = value
            
            # solve rest of board recursively
            if solve_board(board):
                return True
        
        # backtrack
        board[row_ind][col_ind] = 0
    
    # no solution
    return False