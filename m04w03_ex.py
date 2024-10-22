import numpy as np
import matplotlib.pyplot as plt
import random
import secrets

# mục đích để tái lập lại các giá trị tham số ngẫu nhiên (reproducibility)
# random.seed(0)

# ------------load data------------


def load_data_from_file(file_name):
    data = np.genfromtxt(file_name, delimiter=',', dtype=None, skip_header=1)
    features = data[:, :3]
    one_array = np.ones((len(features), 1))
    features_x = np.hstack((one_array, features))
    sale_y = data[:, 3]
    return features_x, sale_y


# ------------create a single theta------------
def create_individual(n=4, bound=10):
    individual = []
    for _ in range(n):
        individual.append(round(random.uniform(-bound/2, bound/2), 2))
    return individual

# ------------create a population------------


def intial_population(m_individual=20, n_gen=4):
    population = [create_individual(n_gen) for _ in range(m_individual)]
    return population


def sort_population(population, feature_x, sales_y):
    fitness_value = [compute_finess(feature_x, sales_y, individual)
                     for individual in population]
    index_sort = np.argsort(fitness_value)
    sorted_population = np.array(population)[index_sort]
    return sorted_population.tolist()


# ------------compute fitness function------------
def compute_loss(feature_x, sales_y, individual):
    n = len(feature_x)
    theta = np.array(individual)
    y_hat = feature_x.dot(theta.T)
    loss = ((y_hat - sales_y.T).T.dot(y_hat - sales_y.T))/(n)
    return loss.item()


def compute_finess(feature_x, sales_y, individual):
    loss = compute_loss(feature_x, sales_y, individual)
    fitness_value = 1/(loss+1)
    return fitness_value

# ------------selection------------


def select_good_individual(sorted_population, m=100):
    index1 = secrets.randbelow(m-1)
    while True:
        index2 = secrets.randbelow(m-1)
        if (index2 != index1):
            break
    selected = sorted_population[index1]
    if index2 > index1:
        selected = sorted_population[index2]
    return selected

# ------------crossover------------


def crossover(individual1, individual2, crossover_rate=0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()
    for i in range(len(individual1)):
        bound = max(np.abs(individual1)).item() + 1
        if random.uniform(-bound, bound) < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]
    return individual1_new, individual2_new


# ------------mutation------------
def mutation(individual, mutation_rate=0.05):
    individual_m = individual.copy()
    for i in range(len(individual)):
        if individual_m[i] < mutation_rate:
            individual_m[i] = random.uniform(-5, 5)
    return individual_m


# ------------create a new population------------
def create_new_population(sorted_population, elitism=2):
    m = len(sorted_population)
    new_population = []
    while len(new_population) < m - elitism:
        # selection
        selection1 = select_good_individual(sorted_population)
        # crossover
        individual1, individual2 = crossover(selection1, sorted_population[-1])
        # mutation
        individual1_m = mutation(individual1)
        individual2_m = mutation(individual2)
        new_population.append(individual1_m)
        new_population.append(individual2_m)
    # copy elitism chromsomes into the next generation
    new_population = new_population + sorted_population[-elitism:]
    return new_population


if __name__ == "__main__":
    n_generations = 100
    m_individual = 600
    features_x, sales_y = load_data_from_file('dataset/advertising.csv')
    population = intial_population(m_individual)
    lost_list = []
    best_list = []
    for gen in range(n_generations):
        print('Generation:', gen)
        sorted_population = sort_population(population, features_x, sales_y)
        loss = compute_loss(features_x, sales_y, sorted_population[-1])
        lost_list.append(loss)
        best_list.append(sorted_population[-1])
        population = create_new_population(sorted_population)
    print(loss, sorted_population[-1])

    plt.plot(lost_list)
    plt.title("find the best model using Genetic Algorithm")
    plt.xlabel("Generations")
    plt.ylabel("Losses")
    plt.show()
