# 3 Step Process:
# Create a population of N elements
# Calculate fitness of N elements, reproduce n times
# Selection
import string
import random

def population(guess, num):
    count = 0
    words = []
    target_length = len(guess)
    while count < num:
        letters = []
        for i in range(target_length):
            letters.append(random.choice(string.ascii_lowercase))
        random_string = "".join(letters)
        count += 1
        words.append(random_string)
    return words

def evaluate(guess, words):
    scores = []
    for word in words:
        score = 0
        for i in range(len(word)):
            if word[i] == guess[i]:
                score += 1
        scores.append(score)
    return scores


def mating(scores, words):
    pool = []
    for i in range(len(words)):
        word = words[i]
        score = scores[i]
        for j in range(score):
            pool.append(word)
    return pool

def crossover(pool):
    parent1 = random.choice(pool)
    parent2 = random.choice(pool)
    split = random.randint(1, len(parent1) - 1)
    child_letters = []
    for i in range(len(parent1)):
        if i < split:
            child_letters.append(parent1[i])
        else:
            child_letters.append(parent2[i])
    child_letters = mutation(child_letters)
    return "".join(child_letters)

def mutation(child_letters):
    random_number = 2 
    for i in range(len(child_letters)):
        ticket = random.randint(1,100)
        if ticket == random_number:
            child_letters[i] = random.choice(string.ascii_lowercase)
    return child_letters

def generation(target, population_size):
    words = population(target, population_size)
    generation_count = 0

    while True:
        scores = evaluate(target, words)
        best_score = max(scores)
        best_word = words[scores.index(best_score)]
        print(generation_count, best_word, best_score)

        if best_score == len(target):
            break

        pool = mating(scores, words)

        if len(pool) == 0:
            words = population(target, population_size)
        else:
            new_words = []
            for i in range(population_size):
                child = crossover(pool)
                new_words.append(child)
            words = new_words

        generation_count += 1

    return best_word

generation("charlie", 100000)

