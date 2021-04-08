import numpy as np

""" Calcule du coût d'une solution """
def cout_solution(dist, solution, n):
    s = solution - 1
    d = 0
    for k in range(n - 1):
        d = d + dist[int(s[k])][int(s[k + 1])]
    d = d + dist[int(s[n - 1])][int(s[0])]
    return d

""" Détermination du voisinage d'une solution en inversant le sens de parcours d’une arête """
def voisinage(solution,n):
    voisininage_ = []
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution) - 1):
            une_solution = np.copy(solution)
            une_solution[i], une_solution[j] = solution[j], solution[i]
            voisininage_.append(une_solution)
    return voisininage_

""" L'algorithme de recherche locale """
def recherche_local(dist, solution_initial,cout_initial,n):
    s_etoile = np.copy(solution_initial)
    z = cout_initial

    condition = True

    while condition:
        condition = False
        voisinage_ = voisinage(s_etoile, n)
        for v in voisinage_:
            if cout_solution(dist,v,n) < z:
                condition = True
                z = cout_solution(dist,v,n)
                s_etoile = np.copy(v)

    return s_etoile, z
