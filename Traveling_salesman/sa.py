import random
import math
import numpy as np

def perturb_tour(tour):
    i, j = random.sample(range(len(tour)), 2)
    new_tour = tour.copy()
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def cooling_schedule(T):
    return 0.99 * T

def simulated_annealing(init_state, eval_func, T, max_iter):
    state = init_state
    state_eval = eval_func(state)
    best_state = state
    best_eval = state_eval

    for _ in range(max_iter):
        T = cooling_schedule(T)
        if T == 0:
            break

        new_state = perturb_tour(state)
        new_eval = eval_func(new_state)
        delta_eval = new_eval - state_eval

        if delta_eval < 0  or random.random() < math.exp(-delta_eval / T):
            state = new_state

            if new_eval < best_eval:
                best_state = state
                best_eval = new_eval

    return best_state, best_eval

def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

def total_distance(cities, tour):
    dist = 0
    for i in range(len(tour) - 1):
        dist += distance(cities[tour[i]], cities[tour[i + 1]])
    dist += distance(cities[tour[-1]], cities[tour[0]])
    return dist

cities = np.random.rand(10, 2)
init_tour = list(range(len(cities)))

best_tour, best_dist = simulated_annealing(init_tour, lambda tour: total_distance(cities, tour), T=100, max_iter=10000)

print("Лучший маршрут:", best_tour)
print("Расстояние:", best_dist)