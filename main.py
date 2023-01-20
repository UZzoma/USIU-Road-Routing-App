# import math
import operator
import random
# from secrets import randbelow
# import numpy as np
from termcolor import cprint, colored

# from scipy import rand

class Environment():
    # start = "76"
    # goal = "118"
    myGraph = {
        "6": set(["83", "8", "157", "44", "15"]),
        "83": set(["6", "8", "47"]),
        "47": set(["107", "109", "141", "8", "83"]),
        "8": set(["83", "6", "9", "47"]),
        "9": set(["8", "12", "157"]),
        "109": set(["108", "12", "47"]),
        "157": set(["9", "44", "6"]),
        "73": set(["107", "68", "156", "130", "10", "15"]),
        "107": set(["73", "105", "47", "141"]),
        "44": set(["6", "157", "15", "108"]),
        "156": set(["130", "73", "108", "68", "15"]),
        "130": set(["10", "156", "73", "68", "108", "15"]),
        "10": set(["130", "73", "68", "112", "99", "119"]),
        "141": set(["2", "144", "47", "107"]),
        "2": set(["141", "144", "99"]),
        "99": set(["2", "119", "112", "10", "68", "105"]),
        "112": set(["119", "99", "10", "87", "68"]),
        "87": set(["139", "119", "126", "112"]),
        "155": set(["126", "139", "127"]),
        "69": set(["76", "127"]),
        "144": set(["2", "141"]),
        "68": set(["105", "73", "99", "130", "119", "108", "156", "10", "112"]),
        "12": set(["108", "9", "109"]),
        "108": set(["12", "109", "73", "15", "130", "156", "10", "68", "44"]),
        "119": set(["87", "99", "112", "10"]),
        "127": set(["139", "155", "69", "54", "118", "126"]),
        "139": set(["127", "87", "126", "155"]),
        "105": set(["107", "68", "99"]),
        "126": set(["139", "155", "127", "87"]),
        "76": set(["69"]),
        "54": set(["127", "118"]),
        "118": set(["54", "127"]),
        "15": set(["6", "44", "108", "73", "130", "156"]),

    }

    carGraph = {
        "6": set(["83"]),
        "83": set(["6", "47"]),
        "47": set(["109", "141", "83"]),
        "9": set(["12"]),
        "108": set(["12", "109"]),
        "109": set(["108", "12", "47"]),
        "141": set(["2", "47"]),
        "2": set(["141", "99"]),
        "99": set(["2", "119", "112"]),
        "112": set(["99", "126"]),
        "69": set(["76", "127", ]),
        "144": set(["2"]),
        "12": set(["109", "9"]),
        "119": set(["99", "112", "126", "127"]),
        "127": set(["54", "118", "69", "119"]),
        "126": set(["127", "119"]),
        "76": set(["69"]),
        "54": set(["127", "118"]),
        "118": set(["54", "127"]),
    }

    location_dict = {
        "6": 'main_gate',
        "83": 'admin_parking',
        "47": 'transport_office',
        "8": 'admin_block',
        "9": 'lilian_beam_building',
        "109": 'cafeteria',
        "157": 'admin_sitting_area',
        "73": 'hostels',
        "107": 'cafelatta',
        "44": 'main_lab',
        "156": 'chandaria_biz_sch',
        "130": 'library',
        "10": 'auditorium',
        "141": 'cafelatta_parking_lot',
        "2": 'bus_park',
        "99": 'basketball_court',
        "112": 'auditorium_parking',
        "87": 'students_centre',
        "155": 'science_complex',
        "69": 'new_school_of_humanities',
        "144": 'visiting_faculty_building',
        "68": 'school_of_comm_and_cinematic_arts',
        "12": 'lilian_beam_parking',
        "108": 'KCB_lilian_beam',
        "119": 'student_centre_parking',
        "127": 'swimming_pool',
        "139": 'swimming_parking',
        "105": 'laundry',
        "126": 'science_complex_parking',
        "76": 'gate_b',
        "54": 'football_pitch',
        "118": 'rugby_field',
        "15": 'school_of_art'
    }

    def display_places(self):
        cprint("*" * 135, "magenta")
        print("*" * 135)
        print()
        cprint(f"{'Check the location mapping:': ^140}", "red")
        print()
        for k, v in Environment.location_dict.items():
            cprint(f"{v :^80} : {k:^80}", 'yellow')

    #  Cost in secs
    cost = {
        str(["6", "83"]): "60", str(["6", "8"]): "55", str(["6", "157"]): "206", str(["6", "44"]): "178",
        str(["6", "15"]): "240", str(["6", "47"]): "20",
        str(["83", "6"]): "60", str(["83", "8"]): "42", str(["83", "47"]): "54",
        str(["47", "107"]): "75", str(["47", "109"]): "24", str(["47", "141"]): "108", str(["47", "8"]): "92",
        str(["47", "83"]): "54",
        str(["8", "83"]): "42", str(["8", "6"]): "55", str(["8", "9"]): "25", str(["8", "47"]): "92",
        str(["9", "8"]): "25", str(["9", "12"]): "9", str(["9", "157"]): "43",
        str(["109", "108"]): "23", str(["109", "12"]): "26", str(["109", "47"]): "24",
        str(["157", "9"]): "43", str(["157", "44"]): "62", str(["157", "6"]): "206",
        str(["73", "107"]): "28", str(["73", "68"]): "65", str(["73", "156"]): "91", str(["73", "130"]): "107",
        str(["73", "10"]): "116", str(["73", "15"]): "110",
        str(["107", "73"]): "28", str(["107", "105"]): "27", str(["107", "47"]): "75", str(["107", "141"]): "62",
        str(["44", "6"]): "178", str(["44", "157"]): "62", str(["44", "15"]): "51", str(["44", "108"]): "69",
        str(["156", "130"]): "67", str(["156", "73"]): "91", str(["156", "108"]): "120", str(["156", "68"]): "124",
        str(["156", "15"]): "135",
        str(["130", "10"]): "24", str(["130", "156"]): "67", str(["130", "73"]): "107", str(["130", "68"]): "75",
        str(["130", "108"]): "136", str(["130", "15"]): "150",
        str(["10", "130"]): "24", str(["10", "73"]): "116", str(["10", "68"]): "59", str(["10", "112"]): "68",
        str(["10", "99"]): "71", str(["10", "119"]): "61",
        str(["141", "2"]): "14", str(["141", "144"]): "35", str(["141", "47"]): "108", str(["141", "107"]): "62",
        str(["2", "141"]): "14", str(["2", "144"]): "13", str(["2", "99"]): "66",
        str(["99", "2"]): "66", str(["99", "119"]): "17", str(["99", "112"]): "64", str(["99", "10"]): "71",
        str(["99", "68"]): "70", str(["99", "105"]): "89",
        str(["112", "119"]): "64", str(["112", "99"]): "64", str(["112", "10"]): "68", str(["112", "87"]): "88",
        str(["112", "68"]): "78",
        str(["87", "139"]): "30", str(["87", "119"]): "82", str(["87", "126"]): "54", str(["87", "112"]): "88",
        str(["155", "126"]): "85", str(["155", "139"]): "50", str(["155", "127"]): "44",
        str(["69", "76"]): "98", str(["69", "127"]): "95",
        str(["144", "2"]): "13", str(["144", "141"]): "35", str(["144", "15"]): "35",
        str(["87", "139"]): "24", str(["87", "119"]): "41", str(["87", "126"]): "54", str(["87", "112"]): "81",
        str(["68", "105"]): "22", str(["68", "73"]): "65", str(["68", "99"]): "70", str(["68", "130"]): "75",
        str(["68", "119"]): "44", str(["68", "108"]): "80", str(["68", "156"]): "124", str(["68", "10"]): "59",
        str(["68", "112"]): "78",
        str(["12", "108"]): "10", str(["12", "9"]): "9", str(["12", "109"]): "26",
        str(["108", "12"]): "10", str(["108", "109"]): "23", str(["108", "73"]): "54", str(["108", "15"]): "79",
        str(["108", "130"]): "136", str(["108", "156"]): "120", str(["108", "10"]): "105 ", str(["108", "68"]): "80",
        str(["108", "44"]): "69", str(["108", "107"]): "69",
        str(["119", "87"]): "82", str(["119", "99"]): "17", str(["119", "112"]): "64", str(["119", "10"]): "61",
        str(["127", "139"]): "62", str(["127", "155"]): "44", str(["127", "69"]): "95", str(["127", "54"]): "382",
        str(["127", "118"]): "381", str(["127", "126"]): "108",
        str(["139", "127"]): "62", str(["139", "87"]): "30", str(["139", "126"]): "42", str(["139", "155"]): "50",
        str(["105", "107"]): "27", str(["105", "68"]): "22", str(["105", "99"]): "89",
        str(["126", "139"]): "42", str(["126", "155"]): "85", str(["126", "127"]): "108", str(["126", "87"]): "54",
        str(["76", "69"]): "98",
        str(["54", "127"]): "382", str(["54", "118"]): "117",
        str(["118", "54"]): "117", str(["118", "127"]): "381",
        str(["15", "6"]): "240", str(["15", "44"]): "51", str(["15", "108"]): "79", str(["15", "73"]): "110",
        str(["15", "130"]): "150", str(["15", "156"]): "135",
    }

    vh_cost = {
        str(["6", "83"]): "60",
        str(["83", "6"]): "60", str(["83", "47"]): "54",
        str(["47", "109"]): "24", str(["47", "141"]): "108", str(["47", "83"]): "54",
        str(["9", "12"]): "9",
        str(["108", "12"]): "10", str(["108", "109"]): "23",
        str(["109", "108"]): "23", str(["109", "12"]): "26", str(["109", "47"]): "24",
        str(["141", "2"]): "14", str(["141", "47"]): "108",
        str(["2", "141"]): "14", str(["2", "99"]): "66",
        str(["99", "2"]): "66", str(["99", "119"]): "17", str(["99", "112"]): "64",
        str(["112", "99"]): "64", str(["112", "126"]): "128",
        str(["69", "76"]): "98", str(["69", "127"]): "95",
        str(["144", "2"]): "13",
        str(["12", "109"]): "26", str(["12", "9"]): "9",
        str(["119", "99"]): "17", str(["119", "112"]): "64",
        str(["127", "54"]): "382", str(["127", "118"]): "381", str(["127", "69"]): "95",
        str(["126", "127"]): "108",
        str(["76", "69"]): "98",
        str(["54", "127"]): "382", str(["54", "118"]): "117",
        str(["118", "54"]): "117", str(["118", "127"]): "381",
    }

    def convert(q: list):
        l = []
        for i in q:
            if str(i) in Environment.location_dict.keys():
                l.append(Environment.location_dict[i])
        cprint(l, "green")

    def getCar():
        hour = []
        cars = []
        for i in range(24):
            hour.append(str(i))
        # generate cars for each tme period
        for x in hour:
            # print(x)
            if int(x) < 6:
                car = random.randint(0, 5)
                cars.append(str(car))
            elif int(x) >= 6 and int(x) < 12:
                car = random.randint(0, 15)
                cars.append(str(car))
            elif int(x) >= 12 and int(x) < 16:
                car = random.randint(0, 25)
                cars.append(str(car))
            elif int(x) >= 16 and int(x) < 20:
                car = random.randint(0, 15)
                cars.append(str(car))
            elif int(x) >= 20 and int(x) < 25:
                car = random.randint(0, 5)
                cars.append(str(car))
        return cars[15]

    carHeuristic = {}

    key_nodes = [6, 83, 47, 8, 9, 109, 157, 73, 107, 44, 156, 130, 10, 141, 2, 99, 112, 87, 155, 69, 144, 68, 12, 108, \
                 119, 127, 139, 105, 126, 76, 54, 118, 15]
    for i in key_nodes:
        carHeuristic[str(i)] = getCar()
    # print("carH")
    # print(carHeuristic)

    g_heuristics = {
        "6": ["475"],
        "83": ["212"],
        "47": ["120"],
        "8": ["165"],
        "9": ["148"],
        "109": ["109"],
        "157": ["148"],
        "73": ["65"],
        "107": ["64"],
        "44": ["207"],
        "156": ["125"],
        "130": ["105"],
        "10": ["72"],
        "141": ["69"],
        "2": ["79"],
        "99": ["55"],
        "112": ["90"],
        "87": ["143"],
        "155": ["253"],
        "69": ["324"],
        "144": ["89"],
        "68": ["10"],
        "12": ["142"],
        "108": ["130"],
        "119": ["69"],
        "127": ["278"],
        "139": ["183"],
        "105": ["45"],
        "126": ["204"],
        "76": ["454"],
        "54": ["888"],
        "118": ["940"],
        "15": ["204"]
    }


class Agent(Environment):

    def getCost(pathtoCost):
        pathCost = 0
        i = 0
        while i < len(pathtoCost) - 1:
            l = []
            l.append(pathtoCost[i])
            l.append(pathtoCost[i + 1])
            pathCost = pathCost + int(Environment.cost[str(l)])  # Read the cost between the nodes
            i += 1
        return pathCost

    def get_vh_cost(pathtoCost):
        pathCost = 0
        i = 0
        while i < len(pathtoCost) - 1:
            l = []
            l.append(pathtoCost[i])
            l.append(pathtoCost[i + 1])
            pathCost = pathCost + int(Environment.vh_cost[str(l)])  # Read the cost between the nodes
            i += 1
        return pathCost

    def getH(vertex, goal):
        v = []
        g = []
        for i in Environment.g_heuristics[vertex]:
            v.append(int(i))
            # print(v)
        for i in Environment.g_heuristics[goal]:
            # print(g)
            g.append(int(i))

        heu = abs(v[0] - g[0])  # + abs(v[1] - g[1])
        # print(v[-1])
        # print(g[-1])
        return heu

    def Astar(graph, start, goal):
        p = []
        p.append(start)
        while True:
            ngh = graph[start]
            h = {}
            for i in ngh.difference(p):
                l = []
                l.append(str(start))
                l.append(str(i))
                h[i] = Agent.getH(i, goal) + Agent.getCost(l)

            sortedH = sorted(h.items(), key=operator.itemgetter(1))
            # print(sortedH)
            x = next(iter(sortedH[0]))
            # print(f'x = {x}')
            p.append(x)
            # print(f'p = {p}')
            if x == goal:
                return Environment.convert(p)
            else:
                start = x

    def bfs(graph, start, goal):
        stack = [(start, [start])]
        p = []
        while stack:
            (vertex, path) = stack.pop(0)
            for next in graph[vertex] - set(path):  # remove position in graph we have visited
                if next == goal:
                    p.append(path + [next])
                    return Environment.convert(p[0])
                else:
                    stack.append((next, path + [next]))
        return "The path you have choosen is not correct"

    def gbfs(graph, start, goal):
        p = []
        p.append(start)
        # p = [start]
        while True:
            neighbour = graph[start]
            heurs = {}
            for i in neighbour.difference(p):  # go to neighbours except those visited
                heurs[i] = Agent.getH(i, goal)

            sorted_heurs = sorted(heurs.items(), key=operator.itemgetter(1))
            x = next(iter(sorted_heurs[0]))
            p.append(x)
            if x == goal:
                return p
            else:
                start = x

    def ucs(graph, start, goal):
        stack = [(start, [start])]
        p = []
        least_cost = 5000

        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):  # remove position in graph we have visited
                if next == goal:
                    path_cost = Agent.getCost(path + [next])
                    print("UCS Path: ", path + [next], "Path Cost: ", path_cost)
                    print("\n")
                    if path_cost < least_cost:
                        least_cost = path_cost
                        p = path + [next]
                else:
                    stack.append((next, path + [next]))
        return p

    def vh_ucs(graph, start, goal):
        stack = [(start, [start])]
        p = []
        least_cost = 5000

        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):  # remove position in graph we have visited
                if next == goal:
                    path_cost = Agent.get_vh_cost(path + [next])
                    print("UCS Path: ", path + [next], "Path Cost: ", path_cost)
                    print("\n")
                    if path_cost < least_cost:
                        least_cost = path_cost
                        p = path + [next]
                else:
                    stack.append((next, path + [next]))
        return p

    def path(self, choice, Start, Goal):
        if choice == "a" or choice == "A":
            cprint(f'Going by foot. Follow the route below to your destination: ', 'yellow')
            print()
            print(f'{Agent.Astar(Environment.myGraph, Start, Goal)}')
            cprint("-" * 135, "red")
        if choice == "b" or choice == "B":
            cprint(f"Going by vehicle. Follow the route below to your destination: ", 'yellow')
            print()
            print(f'{Agent.bfs(Environment.carGraph, Start, Goal)}')
            cprint("-" * 135, "red")

    def __init__(self, Environment):

        cprint("*" * 135, "grey")
        cprint("*" * 135, "cyan")
        cprint(f"{'USIU MAP NAVIGATOR' : ^140}", "red")
        Environment.display_places()
        cprint("*" * 135, "red")
        print()
        starts = input("What is your current position? (Enter map location number) ")
        goals = input("Where are you going? (Enter map location number) ")
        print()
        print("-" * 135)
        cprint("What is your mode of travel? ", "cyan")
        cprint("A: Walking", "blue")
        cprint("B: vehicle", "magenta")
        print()
        way = input("Travel mode: ")
        cprint("-" * 135, "red")
        print()
        Agent.path(self=Environment, choice=way, Start=starts, Goal=goals)
        # print("Astar", Agent.Astar(Environment.myGraph, Environment.start, Environment.goal))
        # print("BFS", Agent.bfs(Environment.carGraph, Environment.start, Environment.goal))
        # print("\n")
        # print("UCS", Agent.vh_ucs(Environment.carGraph, Environment.start, Environment.goal))
        # print("\n")
        # print("UCS", Agent.ucs(Environment.carGraph, Environment.start, Environment.goal))
        # print("\n")
        # print("\n")
        # print("Astar", Agent.vh_Astar(Environment.carGraph, Environment.start, Environment.goal))
        # print("\n")


theEnvironment = Environment()
theAgent = Agent(theEnvironment)


