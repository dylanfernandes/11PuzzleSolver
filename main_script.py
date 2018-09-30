import heapq
from SearchTree import TreeNode

# constants
GOAL_STATE = 0
COST_PER_MOVE = 1

# Also include file I/O for the execution output


def main():
    """ Main code goes here"""
    ...

# Other methods


def heuristic_1(puzzle):
    ...


def heuristic_2(puzzle):
    ...


def depth_first_search():
    ...


def best_first_search(puzzle, heuristic_func):

    # Form auxiliary data structures
    closed_list = []

    # Form priority queue
    open_list = []
    open_list_pq = heapq.heapify(open_list)

    # Form first tree node and add it to queue to begin
    # NOTE: data for nodes is the board/puzzle with an action done to it
    search_tree = TreeNode(puzzle)
    heuristic_value = heuristic_func(search_tree.get_data())
    search_tree.set_heuristic_value(heuristic_value)
    heapq.heappush(open_list_pq, search_tree)

    # Game loop
    while len(open_list_pq) > 0:

        tree_node_to_check = heapq.heappop(open_list_pq)
        closed_list.append(tree_node_to_check)

        # Find better way to check goal state
        if tree_node_to_check.get_heuristic_value() == GOAL_STATE:

            # get solution path to node

            # clear open list to end loop
            while len(open_list_pq) > 0:
                heapq.heappop(open_list_pq)

            return  # the solution
        else:

            # Find add add possible puzzle configs as children to tree_node_to_check here
            # Also use heuristic_func to set their heuristic values

            for child in tree_node_to_check.get_children:
                heapq.heappush(open_list_pq, child)

            if len(open_list_pq) == 0:
                print("Solution not found!")
                return None


def a_star(puzzle, heuristic_func):

    # Form auxiliary data structures
    closed_list = []

    # Form priority queue
    open_list = []
    open_list_pq = heapq.heapify(open_list)

    # Form first tree node and add it to queue to begin
    # NOTE: data for nodes is the board/puzzle with an action done to it
    search_tree = TreeNode(puzzle)
    heuristic_value = heuristic_func(search_tree.get_data())
    search_tree.set_heuristic_value(heuristic_value)
    heapq.heappush(open_list_pq, search_tree)

    # Game loop
    while len(open_list_pq) > 0:

        tree_node_to_check = heapq.heappop(open_list_pq)
        closed_list.append(tree_node_to_check)

        # Find better way to check goal state
        if tree_node_to_check.get_heuristic_value() == GOAL_STATE:

            # get solution path to node

            # clear open list to end loop
            while len(open_list_pq) > 0:
                heapq.heappop(open_list_pq)

            return  # the solution
        else:

            # Find add add possible puzzle configs as children to tree_node_to_check here
            # Also use heuristic_func to set their heuristic values and set cost as well

            for child in tree_node_to_check.get_children:
                heapq.heappush(open_list_pq, child)

            if len(open_list_pq) == 0:
                print("Solution not found!")
                return None


# Execute main here
main()
