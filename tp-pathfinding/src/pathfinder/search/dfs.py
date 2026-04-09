from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        #Verificar Test objetivo <---------------------
        if grid.objective_test(root.state):
            return Solution(root, expanded)

        #Crear la frontera y apilar nodo raiz
        frontier = StackFrontier()
        frontier.add(root)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # TODO Complete the rest!!
        while True:
                
            if frontier.is_empty():
                return NoSolution(expanded)
            
            #Retiro un nodo de la frontera
            node = frontier.remove()

            #Control para evitar expandir un estado ya expandido
            if node.state in expanded: continue
            expanded[node.state] = True #Agregamos el nodo

            #Aplicar todas las acciones posibles
            actions = ["right", "left", "up", "down"]
            for action in actions:
                if action in grid.actions(node.state):
                    # Obtenemos el sucesor
                    successor = grid.result(node.state, action)

                    # Checkeamos que el sucesor no esté en expandidos
                    if successor not in expanded:
                        
                        # Inicializamos el nodo hijo (son)
                        son = Node(
                            "",
                            successor,
                            cost=node.cost + grid.individual_cost(node.state, action),
                            parent=node,
                            action=action,
                        )


                        # Aplicamos el objective test
                        if grid.objective_test(successor):
                            return Solution(son, expanded)

                        #Apilar el nodo en la frontera
                        frontier.add(son)

