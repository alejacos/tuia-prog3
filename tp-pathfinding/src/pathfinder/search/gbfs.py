from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        frontier = PriorityQueueFrontier()
        frontier.add(root,root.distance(grid.end))

        #Iterar mientras la frontera no esté vacía
        while True:
            if frontier.is_empty():
                return NoSolution(reached)
            
            #Retiro un nodo de la frontera
            node = frontier.pop()

            #Verificar Test objetivo
            if grid.objective_test(node.state):
                return Solution(node, reached)

            #Aplicar todas las acciones posibles <---------------------
            actions = ["right", "left", "up", "down"]
            for action in actions:
                if action in grid.actions(node.state):
                    # Obtener el succesor  y su costo
                    successor = grid.result(node.state, action)
                    cost = node.cost + grid.individual_cost(node.state, action)

                    # Checkear si el sucesor está en alcanzados o si el costo es menor
                    if successor not in reached or cost < reached[successor]:
                        # Initialize the son node
                        son = Node(
                            "",
                            successor,
                            cost=cost,
                            parent=node,
                            action=action,
                        )

                        # Cargar el sucesor como alcanzado con su costo
                        reached[successor] = cost
                        #Encolar el nodo en la frontera con su costo
                        frontier.add(son, son.distance(grid.end))
        
       
