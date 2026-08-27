import random
import math

# weights = [1,0,0.5,-0.5,0.25,0.25,2,0.5,1]

genome_length = 9
nudge_size = 0.2
# create sigmoid function - turns any number to 0-1
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# calculates the forward pass using two inputs and weights of hidden layer and output. 
def forward(weights, x1, x2):
    # weights 0-3 hidden layer weights, 4-5 output weights 6-7 hidden layer bias, 8 output bias
    h1 = sigmoid((x1*weights[0]) + (x2 * weights[2]) + weights[6])
    h2 = sigmoid((x1*weights[1]) + (x2*weights[3] + weights[7]))
    output = sigmoid((h1 * weights[4]) + (h2 * weights[5]) + weights[8])
    return output


xor_cases = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]

# calculates mean squred error for all 4 potential outputs of the xor using a set of random weights. Score inverted as bigger = better
def evaluate(population):
    result = []
    for individual in population:
        total = 0
        for x1, x2, target in xor_cases:
            total += (target - forward(individual,x1,x2)) ** 2
        mse = total / len(xor_cases)
        score = 1 / (mse+0.0001)
        result.append(score)

    return result


golden_one = [1, 0, 0.5, -0.5, 0.25, 0.25, 2, 0.5, 1]
golden_two = [1, 0.75, 0.5, -0.5, 0.25, 0.25, 2, 0.5, 1]

# generates a population of length genome_length all with values between -1 and 1 
def population(size):
    individuals = []
    for i in range(size):
        individual = []
        for j in range(genome_length):
            individual.append(random.uniform(-1,1))
        individuals.append(individual)
    return individuals


# creates a raffle based on the score that the list achieved - each ticket individual gets tickets proportional to its score/generations best
def mating(scores, population):
    best = max(scores)
    pool = []
    if best == 0:
        return pool
    for i in range(len(scores)):
        score = scores[i]
        weight_list = population[i]
        tickets = int(((score/best) ** 4) * 100)
        for j in range(tickets):
            pool.append(weight_list)
    return pool

# creates parent1 and parent2 from random selection from the pool created based on tickets 
def crossover(pool):
    child = []
    parent1 = random.choice(pool)
    parent2 = random.choice(pool)
    split = random.randint(1, len(parent1) - 1)
    for i in range(len(parent1)):
        if i < split:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    child = mutation(child)
    return child 

# mutate every child by between -0.2 and 0.2 
def mutation(child):
    figure = random.randint(0, len(child) - 1)
    child[figure] += random.uniform(-nudge_size, nudge_size)
    return child 

def generation(population_size, generations):
    nets = population(population_size)
    best_net = None

    for g in range(generations):
        scores = evaluate(nets)
        best_score = max(scores)
        best_net = nets[scores.index(best_score)]

        print(g, best_score, 1 / best_score)   

        if best_score > 2000:                  
            break
        pool = mating(scores, nets)
        if len(pool) == 0:
            nets = population(population_size)
            continue
        new_nets = []
        new_nets.append(list(best_net))        

        for i in range(population_size - 1):
            child = crossover(pool)
            new_nets.append(child)

        nets = new_nets


    print("champion answers:")
    for x1, x2, target in xor_cases:
        print(x1, x2, "->", forward(best_net, x1, x2), "want", target)

    return best_net


generation(300, 2000)






    


