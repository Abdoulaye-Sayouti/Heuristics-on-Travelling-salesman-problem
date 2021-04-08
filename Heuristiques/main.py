import numpy as np
import time
from heuristique_constructive import heuristique_du_plus_proche_voisin
from heuristique_recherche_locale import recherche_local

""" Lecture de la matrice des distances à partir des fichiers """


def read_dist(filename, n):
    dist = np.zeros((n, n))

    file1 = open(filename, 'r')
    Lines = file1.readlines()
    i = 0
    for line in Lines:
        l = line.rstrip("\n").split(' ')
        j = 0
        for k in l:
            if len(k) != 0:
                dist[i][j] = int(float(k))
                j = j + 1
        i = i + 1
    return dist


""" Calcule du coût d'une solution """


def cout_solution(dist, solution, n):
    s = solution - 1
    d = 0
    for k in range(n - 1):
        d = d + dist[int(s[k])][int(s[k + 1])]
    d = d + dist[int(s[n - 1])][int(s[0])]
    return d


""" Fonction principale """
if (__name__ == '__main__'):
    data_name = ['Data/five_d.txt', 'Data/gr17_d.txt', 'Data/fri26_d.txt', 'Data/att48_d.txt']
    data_size = [5, 17, 26, 48]

    """ k est compris entre 0 et 3"""
    k = 3
    dist = read_dist(data_name[k], data_size[k])
    print(dist)

    """  Application de l'heuristique du plus proche voisin  """
    print("\nApplication de l'heuristique du plus proche voisin")
    start_time1 = time.time()
    solution1 = heuristique_du_plus_proche_voisin(dist, data_size[k])
    elapsed_time = time.time() - start_time1
    print("solution = ", solution1, " coût =", cout_solution(dist, solution1, data_size[k]), " temps =", elapsed_time)

    """  Application de l'heuristique recherche local  """
    print("\nApplication de l'heuristique recherche local ")
    start_time2 = time.time()
    solution2 = recherche_local(dist, solution1, cout_solution(dist, solution1, data_size[k]), data_size[k])
    elapsed_time = time.time() - start_time2
    print("solution = ", solution2[0], " coût =", solution2[1], " Temps = ", elapsed_time)

  