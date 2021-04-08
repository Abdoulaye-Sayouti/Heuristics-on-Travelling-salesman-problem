import numpy as np
INF = 1000000

def heuristique_du_plus_proche_voisin(dist,n):
    solution = np.zeros(n)
    data = np.copy(dist)

    """ Infinie au niveau des 0 """
    for k in range(n):
        data[k][k] = INF

    """ Sélection du plus proche voisin à chaque fois """
    for k in range(n - 1):
        indexes = np.argsort(data[int(solution[k])])
        for l in indexes:
            if l not in solution:
                solution[k + 1] = l
                break

    return solution + 1
