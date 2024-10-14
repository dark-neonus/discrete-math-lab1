""" Module to work with relations and their matrixes """

def read_matrix(file_name: str) -> tuple[list[list[int]], int]:
    """Read matrix from file and return it with its dimension.

    Args:
        file_name (str): name of file to open.

    Returns:
        tuple[list[list[int]], int]: tuple of matrix of integer
            from file with given name and dimension of matrix.
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        n = len(lines)
        result = []

        for line in lines:
            result.append([])
            for x in range(n):
                result[-1].append(int(line[x]))
        return (result, n)

def save_matrix(file_name: str, matrix: list[list[int]]) -> None:
    """Saves matrix to file with given name

    Args:
        file_name (str): name of the file where to save matrix.
        matrix (list[list[int]]): matrix that should be saved.
    """

    with open(file_name, "w", encoding="utf-8") as file:
        text = ''
        for line in matrix:
            row = ''
            for el in line:
                row += str(el)
            text += row + '\n'
        file.write(text[:-1])

def matrix_to_relation(set_of_elements: list[object],
                        matrix: list[list[int]]) -> list[object]:
    """ Convert matrix to corresponding relation

    Args:
        set_of_elements (list[object]): source set of relation
        matrix (list[list]): matrix that represent relation

    Returns:
        list[object]: relation corresponding to given matrix

    Examples:
    >>> matrix_to_relation([2, 4, 6],
    ... [[1, 0, 0],
    ...  [0, 1, 1],
    ...  [0, 1, 0]])
    [(2, 2), (4, 4), (4, 6), (6, 4)]
    """
    relation = []
    for y, row in enumerate(matrix):
        for x, is_presented in enumerate(row):
            if is_presented:
                relation.append( (set_of_elements[y], set_of_elements[x]) )

    return relation

def relation_to_matrix(set_of_elements: list[object],
                        relation: list[tuple[object, object]]) -> list[list[int]]:
    """ Convert relation to corresponding matrix

    Args:
        set_of_elements (list[object]): source set of relation
        relation (list[tuple[object, object]]): relation that represent matrix

    Returns:
        list[list[int]]: matrix that represent given relation

    Example:
    >>> relation_to_matrix([2, 4, 6], [(2, 2), (4, 4), (4, 6), (6, 4)])
    [[1, 0, 0], [0, 1, 1], [0, 1, 0]]
    """
    matrix = []
    for el_a in set_of_elements:
        matrix.append([])
        for el_b in set_of_elements:
            matrix[-1].append( int((el_a, el_b) in relation) )

    return matrix

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
