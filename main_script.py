import heapq
import sys
from SearchTree import TreeNode
from board import Board

# constants
GOAL_STATE = [1,2,3,4,5,6,7,8,9,10,11,0]
COST_PER_MOVE = 1
# The erroneous heuristic value is the largest possible int to guarantee it not being used (REMOVE WHEN NOT NEEDED)
ERRONEOUS_HEURISTIC = sys.maxint

# Also include file I/O for the execution output


def main():
    """ Main code goes here"""
    board = Board(8, 1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11)
    best_first_search(board, heuristic_2)
    # print(board.determineMoves())
    # board.printBoard()
    # board.makeMove(2)
    # print(board.determineMoves())
    # board.printBoard()
    # board.makeMove(2)
    # board.printBoard()

    # pass

# Other methods


def heuristic_1(puzzle, move=-1):
    heuristic_value = 0
    if move >= 0:
        puzzle.makeMove(move)
    return ERRONEOUS_HEURISTIC


def heuristic_2(puzzle, move=-1):
    """
    This heuristic does the following:
    For each piece, it determines the number of pieces currently adjacent to it that are
    NOT supposed to be adjacent to it in the goal state. Then the sum of all of those values will be returned.
    NOTE: Will not check diagonally adjacent pieces.
    :param puzzle: an instance of a board
    :param move: the move to perform in order to evaluate its heuristic
    :return: the heuristic value, which is the total number of pieces that are not in their correct positions.
    """
    heuristic_value = 0
    # Give the option of calculating the heuristic value without making a move
    if move >= 0:
        puzzle.makeMove(move)

    for element in puzzle.getElements():
        # Get the containing row and column of the current element
        element_row = puzzle.getElementRow(element)
        element_col = puzzle.getElementColumn(element)

        element_row_index = element_row.index(element)
        element_col_index = element_col.index(element)

        # The indices of the adjacent elements will be checked, and will be ignored if the piece
        # is not supposed to have elements in certain adjacent spots

        # Check the elements on the right and left
        left_index = element_row_index - 1
        right_index = element_row_index + 1

        # Edge case: the 0-piece -> this will be assigned a value of 12 for the comparisons to make sense
        if element == 0:
            element = 12

        if left_index > 0:
            if element_row[left_index] != element - 1:
                heuristic_value += 1

        if right_index < len(element_row):
            if element_row[right_index] != element + 1:
                heuristic_value += 1

        # Check the elements above and below
        top_index = element_col_index - 1
        bot_index = element_col_index + 1

        if top_index > 0:
            if element_col[top_index] != element - puzzle.ROWSIZE:
                heuristic_value += 1

        if bot_index < len(element_col):
            if element_col[bot_index] != element + puzzle.ROWSIZE:
                heuristic_value += 1

        return heuristic_value


def depth_first_search(puzzle):
    open_list = []
    closed_list = []
    while not open_list:
        current = open_list.pop(0)
        if tree_node_to_check.get_heuristic_value() == GOAL_STATE:
            # get solution path to node
            print("SOLVED!")
            puzzle.printBoard()
            print("Solution " + str(get_solution_path(tree_node_to_check)))
        else:
            #create nodes for each valid moves
            closed_list.append(current)
            #delete children already in open or closed
            #add other children at start of open
    print("Solution not found!")
    return None


def best_first_search(puzzle, heuristic_func):
    return search_with_priority(puzzle, heuristic_func, 0)


def a_star(puzzle, heuristic_func):
    return search_with_priority(puzzle, heuristic_func, COST_PER_MOVE)


def search_with_priority(puzzle, heuristic_func, cost_per_move):

    # Form auxiliary data structures
    closed_list = []

    # Form priority queue
    open_list = []
    open_list_pq = heapq.heapify(open_list)

    # Form first tree node and add it to queue to begin
    search_tree = TreeNode(0)
    heuristic_value_root = heuristic_func(puzzle)
    search_tree.set_heuristic_value(heuristic_value_root)
    heapq.heappush(open_list_pq, search_tree)

    # Game loop
    while len(open_list_pq) > 0:

        tree_node_to_check = heapq.heappop(open_list_pq)
        closed_list.append(tree_node_to_check)

        puzzle.makeMove(tree_node_to_check.get_data())

        # Find better way to check goal state
        if tree_node_to_check.get_heuristic_value() == GOAL_STATE:

            # get solution path to node
            print("SOLVED!")
            puzzle.printBoard()
            print("Solution " + str(get_solution_path(tree_node_to_check)))

            # clear open list to end loop
            while len(open_list_pq) > 0:
                heapq.heappop(open_list_pq)

            return None  # the solution
        else:

            # Find add add possible puzzle configs as children to tree_node_to_check here
            # Also use heuristic_func to set their heuristic values and set cost as well
            possible_moves = puzzle.determineMoves()
            for move in possible_moves:
                heuristic_value = heuristic_func(puzzle, move)
                tree_node_to_check.create_and_add_child_with_cost(move, heuristic_value, cost_per_move)

            for child in tree_node_to_check.get_children:
                heapq.heappush(open_list_pq, child)

            if len(open_list_pq) == 0:
                print("Solution not found!")
                return None


# NOTE: CHANGE TO HAVE STRING REP OF ITEMS
# go up the parents and put them in array
def get_solution_path(leaf_node):
    solution_path = []
    if len(leaf_node.get_children()) == 0:
        curr_tree_node = leaf_node
        while curr_tree_node is not None:
            solution_path.insert(0, curr_tree_node)
            curr_tree_node = curr_tree_node.get_parent()
    return solution_path


# Execute main here
main()
