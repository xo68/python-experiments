from collections import deque


# Create a graph and run BFS
def bfs():
    graph = {}
    queue = deque()
    checked = []

    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["tom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = []

    queue += graph["you"]
    while queue:
        # print(f"check:{checked}")
        person = queue.popleft()

        # We ensure that we have not yet checked the person
        if not person in checked:
            # print(f"Check person:{person}")
            if person_found(person):
                return True
            queue += graph[person]
            checked.append(person)
    return False


def person_found(name):
    return name[-1] == "c"


def run_bfs():
    if bfs():
        print("Person found")
    else:
        print("Person NOT found")


# Dijkstra’s algorithm
def run_dijkstra():

    # Hash Table - Weighted and directed Graph with 4 nodes start, a, b, end
    graph = {}
    graph["start"] = {}
    graph["a"] = {}
    graph["b"] = {}
    graph["end"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"]["end"] = 1
    graph["b"]["a"] = 3
    graph["b"]["end"] = 5

    # Hash Table -  Store the costs of each node
    # How long to is take to go there from the "start"
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["end"] = float("inf")

    # Hash Table - Parents
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None

    processed = []

    node = lowest_costs_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighboors = graph[node]
        for n in neighboors:
            new_cost = cost + neighboors[n]
            if costs[n] > new_cost:  # <-- We found a short path ?
                costs[n] = new_cost  # Update the cost to that node
                parents[n] = node  # Update the parent of that node
        processed.append(node)
        node = lowest_costs_node(costs, processed)
    print(f"All sortest paths: {costs}")
    print(f"All parents: {parents}")


# Required for Dijkstra’s algorithm
def lowest_costs_node(costs, processed):
    lowest = float("inf")
    node = None
    for n in costs:
        print(f"n is :{n}")
        cost = costs[n]
        if cost < lowest and n not in processed:
            lowest = cost
            node = n
    return node


if __name__ == "__main__":
    run_dijkstra()
    # run_bfs()
