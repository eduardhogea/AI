from .. problem import Problem
from .. datastructures.priority_queue import PriorityQueue


def get_solver_mapping():
    return dict(ucs=UCS)


class UCS(object):
    # TODO, excercise 2:
    # - implement Uniform Cost Search (UCS), a variant of Dijkstra's Graph Search
    # - use the provided PriorityQueue where appropriate
    # - to put items into the PriorityQueue, use 'pq.put(<priority>, <item>)'
    # - to get items out of the PriorityQueue, use 'pq.get()'
    # - store visited nodes in a 'set()'
    def solve(self, problem: Problem):
        q = PriorityQueue()
        curent_node = problem.get_start_node()
        visited= set()
        q.put(curent_node.cost, curent_node)
        while problem.is_end(curent_node) is False:
            visited.add(curent_node)

            for i in problem.successors(curent_node):
                q.put(i.cost,i)

            curent_node = q.get()
            while curent_node in visited:
                curent_node = q.get()
        return curent_node
