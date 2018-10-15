import heapq
import sys
import itertools
from SearchTree import TreeNode
from board import Board

# constants
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
GOAL_STATE_HEURISTIC_VAL = 0
COST_PER_MOVE = 1
ROOT_LETTER = '0'
# The erroneous heuristic value is the largest possible int to guarantee it not being used (REMOVE WHEN NOT NEEDED)
ERRONEOUS_HEURISTIC = sys.maxint

# Also include file I/O for the execution output


def main():
    """
    Requests user input for the puzzle to solve and executes all of the searches for it.
    Outputs results in output files.
    """

    # Input the board
    board_to_solve = None
    while board_to_solve is None:
        board_to_solve = input_board()

    # Perform all of the searches
    bfs_h1_solution = best_first_search(board_to_solve, heuristic_1)
    print 'See solution in puzzleBFS-h1.txt.\n'

    a_star_h1_solution = a_star(board_to_solve, heuristic_1)
    print 'See solution in puzzleAs-h1.txt.\n'

    bfs_h2_solution = best_first_search(board_to_solve, heuristic_2)
    print 'See solution in puzzleBFS-h2.txt.\n'

    a_star_h2_solution = a_star(board_to_solve, heuristic_2)
    print 'See solution in puzzleAs-h2.txt.\n'

    # Generate the output files
    output_solution_in_file(bfs_h1_solution, 'puzzleBFS-h1.txt')
    output_solution_in_file(a_star_h1_solution, 'puzzleAs-h1.txt')
    output_solution_in_file(bfs_h2_solution, 'puzzleBFS-h2.txt')
    output_solution_in_file(a_star_h2_solution, 'puzzleAs-h2.txt')


# I/O Functions
def input_board():
    """
    Allow the user to input a board configuration. Handles all incorrect cases and makes the user retry each time.
    :return: the correctly entered board
    """
    board_size = Board.getDefSize()
    please_enter_nums_properly_msg = 'Please enter exactly ' + str(board_size) + ' unique numbers, starting at 0 and ' \
                                                                                 'separated by spaces.\n'
    board_config_str = raw_input('Enter the ' + str(board_size - 1) + '-puzzle to solve: ')
    board_config_str_split = board_config_str.split(" ")

    # Handle non-integer input
    try:
        # Converts the input string elements into integer elements
        board_config = [int(s) for s in board_config_str_split]
    except ValueError:
        print 'Error: Invalid input. ', please_enter_nums_properly_msg
        return None

    # Handle incorrect board size
    if len(board_config) < board_size:
        print 'Error: Too few numbers input. ', please_enter_nums_properly_msg
        return None
    elif len(board_config) > board_size:
        print 'Error: Too many numbers input. ', please_enter_nums_properly_msg
        return None
    else:

        # Handle incorrect numbers and duplicates
        for i, element in enumerate(board_config):
            if element < 0 or element >= board_size:
                print 'Error: Incorrect number entered: ', element, '. ', please_enter_nums_properly_msg
                return None
            elif board_config.index(element) != i:  # i.e. if there is duplicate element with a different index
                print 'Error: Duplicate number entered: ', element, '. ', please_enter_nums_properly_msg
                return None

    return Board(board_config)


# Traverse the tree up to the root from the leaf through its parents and put them in an array
def get_solution_path(leaf_node=None):
    solution_path = []

    if leaf_node is None:
        return []

    if len(leaf_node.get_children()) == 0:
        curr_tree_node = leaf_node
        while curr_tree_node is not None:
            solution_path.insert(0, curr_tree_node.get_data())
            curr_tree_node = curr_tree_node.get_parent()
    return solution_path


def output_solution_in_file(leaf_node=None, file_name='output.txt'):
    solution_path = get_solution_path(leaf_node)

    output_file = open(file_name, 'w')

    for solution in solution_path:
        solution_string = ''
        if isinstance(solution, tuple):
            for item in solution:
                solution_string += (str(item) + ' ')
        output_file.write(solution_string + '\n')

    output_file.close()



# Heuristics and search functions

def heuristic_1(board_config, move=-1):
    """
    This heuristic does the following:
    Computes the number of rows and columns that are complete before checking for elements in the appropriate corner 
    and elements in the appropriate place.
    """
    heuristic_value = 0
    incomplete_row = 100
    incomplete_column = 10
    incomplete_corner = 5
    incomplete_element = 1
    solution = Board(GOAL_STATE)
    corners = [0, solution.getRowSize() - 1, solution.getSize() - solution.getRowSize(), solution.getSize() - 1]
    #col_size indicates number of rows on board
    for index in range(0, solution.col_size):
        if solution.getRow(index) != board_config.getRow(index):
            heuristic_value = heuristic_value + incomplete_row
    #all elements in right spot
    if heuristic_value == 0:
        return heuristic_value
    #row_size indicates number of columns on board
    for index in range(0, solution.getRowSize()):
         if solution.getColumn(index) != board_config.getColumn(index):
            heuristic_value = heuristic_value + incomplete_column

    for corner in corners:
        if solution.elements[corner] != board_config.elements[corner]:
            heuristic_value = heuristic_value + incomplete_corner

    for index in range(0, solution.getSize()):
        if solution.elements[index] != board_config.elements[index]:
            heuristic_value = heuristic_value + incomplete_element

    return heuristic_value


def heuristic_2(board_config):
    """
    This heuristic does the following:
    For each piece, it determines the number of pieces currently adjacent to it that are
    NOT supposed to be adjacent to it in the goal state. In addition, it will also check if the piece is in its correct
    row and column. The point system per piece is: 1 point for each piece that is adjacent to it that isn't supposed to
    be adjacent to it, 5 points for the piece not being in the correct row, 5 points for the piece not being in the
    correct column.
    Then the sum of all of those values will be returned.
    NOTE: Will not check diagonally adjacent pieces.
    :param board_config: an instance of a board
    :param move: the move to perform in order to evaluate its heuristic
    :return: the heuristic value, which is the total number of pieces that are not in their correct positions.
    """
    heuristic_value = 0
    points_bad_adjacent_element = 1
    points_incorrect_row_column = 5

    # This number will be used to represent the empty space (element 0)
    # in order for the comparisons to still make sense for it
    zero_equiv_value = len(board_config.getElements())

    for element in board_config.getElements():
        # Get the containing row and column of the current element
        element_row = board_config.getElementRow(element)
        element_col = board_config.getElementColumn(element)

        element_row_index = element_row.index(element)
        element_col_index = element_col.index(element)

        # Edge case: the 0-piece -> this will be assigned a value of 12 for the comparisons to make sense
        if element == 0:
            element = zero_equiv_value

        # Check the piece's location - check it against its intended row and column indices
        correct_row_index = (element - 1) % board_config.getRowSize()
        correct_col_index = int((element - 1) / board_config.getRowSize())

        if element_row_index != correct_row_index:
            heuristic_value += points_incorrect_row_column

        if element_col_index != correct_col_index:
            heuristic_value += points_incorrect_row_column

        # The indices of the adjacent elements will be checked, and will be ignored if the piece
        # is not supposed to have elements in certain adjacent spots

        # Check the elements on the right and left
        left_index = element_row_index - 1
        right_index = element_row_index + 1

        if left_index >= 0:
            left_element = element_row[left_index]

            if left_element == 0:
                left_element = zero_equiv_value

            if left_element != element - 1:
                heuristic_value += points_bad_adjacent_element

        if right_index < len(element_row):
            right_element = element_row[right_index]

            if right_element == 0:
                right_element = zero_equiv_value

            if right_element != element + 1:
                heuristic_value += points_bad_adjacent_element

        # Check the elements above and below
        above_index = element_col_index - 1
        below_index = element_col_index + 1

        if above_index >= 0:
            above_element = element_col[above_index]

            if above_element == 0:
                above_element = zero_equiv_value

            if above_element != element - board_config.getRowSize():
                heuristic_value += points_bad_adjacent_element

        if below_index < len(element_col):
            below_element = element_col[below_index]

            if below_element == 0:
                below_element = zero_equiv_value

            if below_element != element + board_config.getRowSize():
                heuristic_value += points_bad_adjacent_element

    return heuristic_value


def depth_first_search(board_config):
    open_list = [board_config]
    closed_list = []
    while not open_list:
        current = open_list.pop(0)
        if current.printBoard() == GOAL_STATE_HEURISTIC_VAL:
            # get solution path to node
            print("SOLVED!")
            board_config.printBoard()
            # print("Solution " + str(get_solution_path(tree_node_to_check)))
        else:
            #create nodes for each valid moves
            configs = []
            moves = board_config.determineMoves()
            #for move in moves:
                #configs.append()
            closed_list.append(current)
            #delete children already in open or closed
            #add other children at start of open
    print("Solution not found!")
    return None


def best_first_search(board_config, heuristic_func):
    return search_with_priority(board_config, heuristic_func, 0)


def a_star(board_config, heuristic_func):
    return search_with_priority(board_config, heuristic_func, COST_PER_MOVE)


def search_with_priority(board_config, heuristic_func, cost_per_move):

    # Form auxiliary data structures
    closed_list = []

    # Form priority queue
    open_list_pq = []
    heapq.heapify(open_list_pq)

    # Form first tree node and add it to queue to begin
    search_tree = TreeNode((ROOT_LETTER, board_config))
    heuristic_value_root = heuristic_func(board_config)
    search_tree.set_heuristic_value(heuristic_value_root)
    heapq.heappush(open_list_pq, search_tree)

    # Game loop
    while len(open_list_pq) > 0:

        tree_node_to_check = heapq.heappop(open_list_pq)
        closed_list.append(tree_node_to_check)

        # The second element of the tuple is a board configuration
        board_config = tree_node_to_check.get_data()[1]

        # print tree_node_to_check.get_algo_a_value(), board_config.getElements()

        # Find better way to check goal state
        if tree_node_to_check.get_heuristic_value() == GOAL_STATE_HEURISTIC_VAL:

            # get solution path to node
            print("SOLVED!")

            # clear open list to end loop
            while len(open_list_pq) > 0:
                heapq.heappop(open_list_pq)

            return tree_node_to_check
        else:

            # Find add add possible board_config configs as children to tree_node_to_check here
            # Also use heuristic_func to set their heuristic values and set cost as well
            possible_board_configs = board_config.getAllConfigs()
            possible_moves = board_config.determineMoves()

            # iterate over both the moves and the board configurations (which should be the same length)
            for move, move_config in itertools.izip_longest(possible_moves, possible_board_configs):
                heuristic_value = heuristic_func(move_config)
                move_letter = board_config.getPositionLetter(move)
                move_tuple = (move_letter, move_config)
                tree_node_to_check.create_and_add_child_with_cost(move_tuple, heuristic_value, cost_per_move)

            for child in tree_node_to_check.get_children():
                if child not in closed_list:
                    heapq.heappush(open_list_pq, child)

            if len(open_list_pq) == 0:
                print("Solution not found!")
                return None


# Execute main here
if __name__ == '__main__':
    main()
