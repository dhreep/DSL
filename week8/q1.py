class Node:
    def __init__(self, id):
        self.id = id
        self.is_coordinator = False

    def send_message(self, message, to_node):
        print(f"Node {self.id} sends message '{message}' to Node {to_node.id}")

    def receive_message(self, message, from_node):
        print(
            f"Node {self.id} receives message '{message}' from Node {from_node.id}")

    def start_election(self, nodes):
        """Initiate an election process."""
        print(f"Node {self.id} initiates an election.")
        higher_nodes = [node for node in nodes if node.id > self.id]

        # Send election messages to higher nodes
        for higher_node in higher_nodes:
            higher_node.receive_election(self)

    def receive_election(self, initiating_node):
        """Receive an election message and respond accordingly."""
        print(
            f"Node {self.id} receives an election message from Node {initiating_node.id}.")
        if self.is_coordinator or self.id > initiating_node.id:
            print(
                f"Node {self.id} sends an OK message to Node {initiating_node.id}.")
            initiating_node.receive_ok(self)
        else:
            print(
                f"Node {self.id} ignores the election message from Node {initiating_node.id}.")

    def receive_ok(self, responding_node):
        """Receive an OK message and acknowledge the leader."""
        print(
            f"Node {self.id} receives an OK message from Node {responding_node.id}.")
        self.is_coordinator = False
        responding_node.is_coordinator = True
        print(f"Node {responding_node.id} is elected as the new coordinator.")


def simulate_bully_algorithm(nodes):
    # Assuming the highest ID node is the coordinator
    coordinator = max(nodes, key=lambda node: node.id)
    coordinator.is_coordinator = True
    print(f"Node {coordinator.id} is elected as the coordinator.")

    # Simulate the collapse of the coordinator
    coordinator.is_coordinator = False
    # nodes = nodes.pop()
    print(f"Node {coordinator.id} collapses.")

    # Elect a new coordinator
    for node in nodes:
        if node.is_coordinator:
            continue
        node.start_election(nodes)


if __name__ == "__main__":
    # Create nodes with unique IDs
    # Creating 7 nodes with IDs 1 through 7
    nodes = [Node(id) for id in range(1, 8)]
    print(type(nodes))
    # Simulate leader election
    simulate_bully_algorithm(nodes)
