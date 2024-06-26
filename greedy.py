# Set-Covering problem
# - Reach listeners in all 50 US states
# - Decide what stations to play on to reach all listeners
# -> Minimize the number of stations to play on
def greedy():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()
    while states_needed:
        best = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best = station
                states_covered = covered
        final_stations.add(best)
        states_needed -= states_covered
    print(final_stations)


if __name__ == "__main__":
    greedy()
