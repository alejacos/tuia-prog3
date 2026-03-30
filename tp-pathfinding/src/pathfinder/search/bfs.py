from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        #Verificar Test objetivo <---------------------
        if grid.objective_test(root.state):
            return Solution(root, reached)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        # TODO Complete the rest!!<----------------------
        frontier = QueueFrontier()
        frontier.add(root)

        #Iterar mientras la frontera no esté vacía
        while True:
                
            if frontier.is_empty():
                return NoSolution(reached)
            
            #Retiro un nodo de la frontera
            node = frontier.remove()
            
            #Aplicar todas las acciones posibles
            actions = ["right", "left", "up", "down"]
            for action in actions:
                if action in grid.actions(node.state):
                    # Get the successor
                    successor = grid.result(node.state, action)

                    # Check if the successor is reached
                    if successor not in reached:
                        
                        # Initialize the son node
                        son = Node(
                            "",
                            successor,
                            cost=node.cost + grid.individual_cost(node.state, action),
                            parent=node,
                            action=action,
                        )


                        # Apply objective test
                        if grid.objective_test(successor):
                            return Solution(son, reached)

                        # Mark the successor as reached
                        reached[successor] = True
                        #Encolar el nodo en la frontera
                        frontier.add(son)




            """            
            # Checkear si going "right" es posible
            if "right" in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, "right")

                # Check if the successor is reached
                if successor not in reached:
                    
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, "right"),
                        parent=node,
                        action="right",
                    )


                    # Apply objective test
                    if grid.objective_test(successor):
                        return Solution(son, reached)

                    # Mark the successor as reached
                    reached[successor] = True
                    #Encolar el nodo en la frontera
                    frontier.add(son)

            # Checkear si going "left" es posible
            if "left" in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, "left")

                # Check if the successor is reached
                if successor not in reached:
                    
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, "left"),
                        parent=node,
                        action="left",
                    )


                    # Apply objective test
                    if grid.objective_test(successor):
                        return Solution(son, reached)

                    # Mark the successor as reached
                    reached[successor] = True
                    #Encolar el nodo en la frontera
                    frontier.add(son)
                    
            # Checkear si going "up" es posible
            if "up" in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, "up")

                # Check if the successor is reached
                if successor not in reached:
                    
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, "up"),
                        parent=node,
                        action="up",
                    )


                    # Apply objective test
                    if grid.objective_test(successor):
                        return Solution(son, reached)

                    # Mark the successor as reached
                    reached[successor] = True
                    #Encolar el nodo en la frontera
                    frontier.add(son)

            # Checkear si going "down" es posible
            if "down" in grid.actions(node.state):
                # Get the successor
                successor = grid.result(node.state, "down")

                # Check if the successor is reached
                if successor not in reached:
                    
                    # Initialize the son node
                    son = Node(
                        "",
                        successor,
                        cost=node.cost + grid.individual_cost(node.state, "down"),
                        parent=node,
                        action="down",
                    )


                    # Apply objective test
                    if grid.objective_test(successor):
                        return Solution(son, reached)

                    # Mark the successor as reached
                    reached[successor] = True
                    #Encolar el nodo en la frontera
                    frontier.add(son)
                    
            #continue
            """

