from collections import deque


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


if __name__ == "__main__":
    if bfs():
        print("Person found")
    else:
        print("Person NOT found")
