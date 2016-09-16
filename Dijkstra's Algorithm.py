__author__ = 'Paarth Bhasin'
import re
import copy

flights = {}
edges = {}
inf = float('inf')
paths = []
shortestpaths = []


def dijkstra_cheapest_path(start, end):
    copyflights = copy.deepcopy(flights)
    cost = 0
    lowestcost = inf
    previous = None
    path = str(start) + " "
    finalpath = ""

    '''for keys in copyflights:
        for key in copyflights[keys]:
            if copyflights[keys][key] == inf:
                del copyflights[keys][key]'''

    for keys in copyflights:
        del copyflights[keys][keys]


    # del copyflights[start][start]
    u = start
    count = 0
    while len(copyflights[start]) > 0:
        print(count)
        v = min(copyflights[u], key=lambda vertex: float(copyflights[u][vertex]))
        del copyflights[v][u]
        print(v)
        cost += int(copyflights[u][v])
        if count == 0:
            del copyflights[u][v]
            del copyflights[v][u]
        if v == end and cost < lowestcost:
            finalpath = path + str(v)
            path = str(start) + " "
            lowestcost = cost
            u = start
            cost = 0
            count = 0
            continue
        if v == end and not cost < lowestcost:
            cost = 0
            u = start
            path = str(start) + " "
            count = 0
            continue
        if v == inf:
            u = previous
            continue
        path += str(v) + " "
        count += 1
        previous = u
        u = v

    finalpath += str(lowestcost)
    print("Finalpath: " + str(finalpath))

def dijkstra_shortest_path(start, end):
    valid = True
    ended = False
    copyflights = flights.copy()
    path = str(start) + " "
    cost = 0
    assert start in flights

    u = start
    neighbours = copyflights[u].keys()

    for neighbour in neighbours:
        while valid and not ended:
            for n in neighbour:
                if copyflights[u][neighbour] == inf:
                    valid = False
                    u = start
                if neighbour == end:
                    path += str(cost)
                    shortestpaths.append(path)
                    ended = True
                    u = start
                else:
                    cost += copyflights[u][n]
                    path += neighbour + " "
                    u = neighbour
                    neighbour = copyflights[neighbour].keys()
    length = len(shortestpaths[0])
    position = 0
    for i in range(len(shortestpaths)):
        if len(shortestpaths[i]) < length:
            length = len(shortestpaths[i])
            position = i
    return shortestpaths[position]


def main():
    valid = False
    starting = []
    f = open("Flights.txt", 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        line = re.sub(",", "", line)
        words = line.split()
        # print(words[0])
        flights[words[0]] = {}
        flights[words[1]] = {}
        if words[0] not in starting:
            starting.append(words[0])
        if words[1] not in starting:
            starting.append(words[1])

    s = flights.keys()
    print(starting)
    for keys in s:
        for cities in starting:
            flights[keys][cities] = inf

    for line in lines:
        line = re.sub(",", "", line)
        words = line.split()
        for i in range(len(words) - 1):
            if i == 0:
                flights[words[i]][words[i]] = 0
                flights[words[i + 1]][words[i + 1]] = 0
            if i == 1:
                flights[words[i - 1]][words[i]] = words[i + 1]
                flights[words[i]][words[i - 1]] = words[i + 1]
    cities = flights.keys()

    for city in cities:
        edges[city] = 0
    print("")
    print("Adjacency list with cost: ")
    for keys in flights:
        print(str(keys) + ": " + str(flights[keys]))
    print('\n')
    print("Flight routes with cost: ")
    print('\n')
    startcities = flights.keys()

    for line in lines:
        print(line, end="")
    print('\n')
    while not valid:
        start = input("Enter start city: ")
        end = input("Enter end city: ")
        if start in startcities:  # and end in g[start] and g[start][end] != 0:
            valid = True
            dijkstra_cheapest_path(start, end)
            # print(dijkstra_shortest_path(start, end))


if __name__ == "__main__":
    main()
