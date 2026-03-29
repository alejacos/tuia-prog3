from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        frontier.add(root,root.cost)

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
            # Checkear si going "right" es posible
            if "right" in grid.actions(node.state):
                # Obtener el succesor  y su costo
                successor = grid.result(node.state, "right")
                cost = node.cost + grid.individual_cost(node.state, "right")

                # Checkear si el sucesor está en alcanzados o si el costo es menor
                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=cost,
                        parent=node,
                        action="right",
                    )

                    # Cargar el sucesor como alcanzado con su costo
                    reached[successor] = cost
                    #Encolar el nodo en la frontera con su costo
                    frontier.add(son, cost)

            # Checkear si going "up" es posible
            if "up" in grid.actions(node.state):
                # Obtener el succesor  y su costo
                successor = grid.result(node.state, "up")
                cost = node.cost + grid.individual_cost(node.state, "up")

                # Checkear si el sucesor está en alcanzados o si el costo es menor
                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=cost,
                        parent=node,
                        action="up",
                    )

                    # Cargar el sucesor como alcanzado con su costo
                    reached[successor] = cost
                    #Encolar el nodo en la frontera con su costo
                    frontier.add(son, cost)

            # Checkear si going "left" es posible
            if "left" in grid.actions(node.state):
                # Obtener el succesor  y su costo
                successor = grid.result(node.state, "left")
                cost = node.cost + grid.individual_cost(node.state, "left")

                # Checkear si el sucesor está en alcanzados o si el costo es menor
                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=cost,
                        parent=node,
                        action="left",
                    )

                    # Cargar el sucesor como alcanzado con su costo
                    reached[successor] = cost
                    #Encolar el nodo en la frontera con su costo
                    frontier.add(son, cost)

            # Checkear si going "down" es posible
            if "down" in grid.actions(node.state):
                # Obtener el succesor  y su costo
                successor = grid.result(node.state, "down")
                cost = node.cost + grid.individual_cost(node.state, "down")

                # Checkear si el sucesor está en alcanzados o si el costo es menor
                if successor not in reached or cost < reached[successor]:
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=cost,
                        parent=node,
                        action="down",
                    )

                    # Cargar el sucesor como alcanzado con su costo
                    reached[successor] = cost
                    #Encolar el nodo en la frontera con su costo
                    frontier.add(son, cost)

