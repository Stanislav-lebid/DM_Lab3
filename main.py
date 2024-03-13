import itertools
import numpy as np

def readMatrix(opened_file:str)->list:
    counter = opened_file.readline()
    graph = []
    for _ in range(int(counter)):
        readed_line = opened_file.readline()
        readed_list = readed_line.split()
        list_of_elements = []
        for j in readed_list:
            list_of_elements.append(int(j))
        graph.append(list_of_elements)
    return graph

import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_tsp(distance_matrix):
    num_vertices = len(distance_matrix)
    min_distance = float('inf')
    
    # Знайти всі можливі перестановки вершин
    permutations = itertools.permutations(range(num_vertices))
    
    # Оберіть тільки ті перестановки, які є гамільтонівими циклами
    # (тобто маршрути, що проходять через всі вершини)
    hamiltonian_cycles = filter(lambda p: p[-1] == 0, permutations)
    
    for cycle in hamiltonian_cycles:
        distance = 0
        for i in range(num_vertices - 1):
            distance += distance_matrix[cycle[i]][cycle[i+1]]
        distance += distance_matrix[cycle[-1]][cycle[0]]  # Додати відстань з останньої вершини до першої
        
        if distance < min_distance:
            min_distance = distance
    
    return min_distance

if __name__ == "__main__":
    matrix = open("l3-3.txt","r")
    graph = readMatrix(matrix)
    incidence_matrix = np.array(graph)
    
    result = solve_tsp(incidence_matrix)
    print("Total distance of the shortest tour:", result)
