import random 

cities = []
amount_of_cities = 15
for i in range(amount_of_cities):
        x = random.randint(0,200)
        y = random.randint(0,200)
        cities.append((x, y))

def population(population_size, cities):
    routes = []
    for i in range(population_size):
        start_points = list(range(len(cities)))
        random.shuffle(start_points)
        routes.append(start_points)
    return routes

def distance_between(city_a, city_b):
    x1, y1 = city_a
    x2, y2 = city_b
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

def evaluate(routes, cities):
    results = []
    for route in routes:
        distance = 0
        for i in range(len(route) -1):
            distance += distance_between(cities[route[i]],cities[route[i+1]])
        distance += distance_between(cities[route[0]], cities[route[-1]])
        results.append(1/distance)
    return results
        
def mating(scores, routes):
    best = max(scores)
    pool = []
    if best == 0:
        return pool
    for i in range(len(scores)):
         score = scores[i]
         route = routes[i]
         tickets = int(((score / best) ** 4) * 100)
         for j in range(tickets):
            pool.append(route)
    return pool

def crossover(pool):
    parent1 = random.choice(pool)
    parent2 = random.choice(pool)
    split = random.randint(1, len(parent1) - 1)
    child = []
    for i in range(split):
        child.append(parent1[i])
    for city in parent2:
        if city not in child:
            child.append(city)
    mutation(child)
    return child

def mutation(child):
    x = random.randint(0, len(child) -1 )
    y = random.randint(0, len(child) -1 )
    child[x], child[y] = child[y], child[x]
    return child

def generation(cities, population_size, generations):
    routes = population(population_size, cities)

    for g in range(generations):
        scores = evaluate(routes, cities)
        best_score = max(scores)
        best_route = routes[scores.index(best_score)]

        print(g, 1 / best_score)

        pool = mating(scores, routes)

        if len(pool) == 0:
            routes = population(population_size, cities)
            continue

        new_routes = []
        new_routes.append(best_route)

        for i in range(population_size - 1):
            child = crossover(pool)
            new_routes.append(child)

        routes = new_routes

    return best_route

generation(cities, 100, 5000)




