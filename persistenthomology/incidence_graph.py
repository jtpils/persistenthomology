import networkx as nx
import numpy as np


def get_distance_matrix(dataset):
    num_samples = len(dataset)
    distance_array = np.zeros([num_samples, num_samples])
    for i in range(num_samples):
        for j in range(num_samples):
            distance_array[i, j] = np.linalg.norm(dataset[i] - dataset[j])
    return distance_array


def build_incidence_graph(distance_matrix, epsilon):
    incidence_matrix = (distance_matrix < epsilon)
    num_samples = incidence_matrix.shape[0]
    G = nx.Graph()
    G.add_nodes_from(range(num_samples))
    for i in range(num_samples):
        for j in range(i + 1, num_samples):
            if incidence_matrix[i, j]:
                G.add_edge(i, j)
    return G
