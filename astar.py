import math
from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


# please ignore this
def get_solver_mapping():
    return dict(
        astar_ec=ASTAR_Euclidean,
        astar_mh=ASTAR_Manhattan
    )


class ASTAR(object):
    # TODO, Excercise 2:
    # implement A* search (ASTAR)
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - use a 'set()' to store nodes that were already visited
    def solve(self, problem: Problem):
        goal=problem.get_end_node()
        node=problem.get_start_node()
        q = PriorityQueue()
        visited= set()
        q.put(node.cost+self.heuristic(node,goal),node)
        while problem.is_end(node) is False:
            visited.add(node)

            for i in problem.successors(node):
                q.put(i.cost+self.heuristic(i,goal),i)

            node = q.get()
            while node in visited:
                node = q.get()
        return node


# this is the ASTAR variant with the euclidean distance as a heuristic
# it is registered as a solver with the name 'gbfs_ec'

# please note that in an ideal world, this heuristic should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state
class ASTAR_Euclidean(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.sqrt((cy - gy) ** 2 + (cx - gx) ** 2)


# this is the ASTAR variant with the manhattan distance as a heuristic
# it is registered as a solver with the name 'gbfs_mh'

# please note that in an ideal world, this heuristic should actually be part
# of the problem definition, as it assumes domain knowledge about the structure
# of the problem, and defines a distance to the goal state
class ASTAR_Manhattan(ASTAR):
    def heuristic(self, current, goal):
        cy, cx = current.state
        gy, gx = goal.state
        return math.fabs((cy - gy)) + math.fabs(cx - gx)
