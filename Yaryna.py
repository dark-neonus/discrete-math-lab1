def relation_symmetrical_closure(matrix: list[list[int]]) -> list[list[int]]:
    """ changes the matrix to the symmetrical one

    Args:
        matrix (list[list[int]]): matrix that needed to be changed

    Returns:
        list[list[int]]: symmetrical matrix 
    >>> relation_symmetrical_closure([[1, 0, 0, 1], [0, 1, 0, 1],[1, 1, 0, 1], [0, 0, 0, 0]])
    [[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]

    """
    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            if el == 1 and matrix[x][y] != 1:
                matrix[x][y] = 1

    return matrix


def relation_reflective_closure(matrix: list[list[int]]) -> list[list[int]]: 
    """changes the matrix to the reflective one

    Args:
        matrix (list[list[int]]): matrix that needed to be changed

    Returns:
        list[list[int]]: reflective matrix
    >>> relation_symmetrical_closure([[0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 0]]
    """
    n = len(matrix)
    for y in range(n):
        if matrix[y][y] != 1:
            matrix[y][y] = 1

    return matrix

def equivalence_classes(relation: list[list[int]]) -> list[list]:
    """find classes of the equivalence

    Args:
        relation (list[tuple[int]]): reletion where the classes shoud be finded

    Returns:
        list[list]: list of the fined classes of the equivalence

    >>> equivalence_classes([[1, 1], [1, 2], [1, 4], [2, 1], [2, 2],\
    [2, 4], [3, 3], [4, 1], [4, 2], [4, 4]])
    [[1, 2, 4], [3]]
    """
    first_el = set()
    result = []
    for el in relation:
        first_el.add(el[0])
    for i in first_el:
        inventory = []
        for el in relation:
            if i == el[0]:
                inventory.append(el[1])
        if inventory not in result:
            result.append(inventory)
        return result

if __name__ =="__main__":
    import doctest
    print(doctest.testmod())
    