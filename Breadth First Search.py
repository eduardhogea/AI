from .. problem import Problem
from .. datastructures.queue import Queue


# please ignore this
def get_solver_mapping():
    return dict(bfs=BFS)


class BFS(object):
    # TODO, exercise 1:
    # - implement Breadth First Search (BFS)
    # - use 'problem.get_start_node()' to get the node with the start state
    # - use 'problem.is_end(node)' to check whether 'node' is the node with the end state
    # - use a set() to store already visited nodes
    # - use the 'queue' datastructure that is already imported as the 'fringe'/ the 'frontier'
    # - use 'problem.successors(node)' to get a list of nodes containing successor states
    def solve(self, problem: Problem):
        queue = Queue()
        
        curent_node = problem.get_start_node() #assign to curent_node the node with the start state
        visited= set() #a set in which i will store all the visited notes
        
        queue.put(curent_node) #adding the first node to the fringe

        while problem.is_end(curent_node) is False:
            visited.add(curent_node) #adding the visited nodes
                                    
            for i in problem.successors(curent_node):
                queue.put(i) #putting the successors in the fringe
            curent_node = queue.get() #moving to the next node
            while curent_node in visited: #checking to see if the node was already visited
                curent_node = queue.get() 


        
        return curent_node
