""" Module to work with relations and their matrixes """
from copy import deepcopy
import itertools

def read_matrix(file_name: str) -> tuple[list[list[int]], int]:
    """Read matrix from file and return it with its dimension.

    Args:
        file_name (str): name of file to open.

    Returns:
        tuple[list[list[int]], int]: tuple of matrix of integer
            from file with given name and dimension of matrix.

    Example:
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _ = tmpfile.write("011\\n101\\n001\\n")
    >>> read_matrix(tmpfile.name)
    ([[0, 1, 1], [1, 0, 1], [0, 0, 1]], 3)
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        n = len(lines)
        result = []

        for line in lines:
            result.append([int(x) for x in line.strip()])
        return (result, n)

def save_matrix(file_name: str, matrix: list[list[int]]) -> None:
    """Saves matrix to file with given name

    Args:
        file_name (str): name of the file where to save matrix.
        matrix (list[list[int]]): matrix that should be saved.
    
    Example:
    >>> import tempfile
    >>> save_matrix('tmp.txt', [[0, 1, 1], [1, 0, 1], [0, 0, 1]])
    >>> with open('tmp.txt', 'r', encoding='utf-8') as file:
    ...     for line in file:    
    ...         print(line.strip().split())
    ['011']
    ['101']
    ['001']
    """

    with open(file_name, "w", encoding="utf-8") as file:
        text = ''
        for line in matrix:
            row = ''
            for el_ in line:
                row += str(el_)
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

def matrix_transitive_closure(matrix: list[list[int]]) -> list[list[int]]:
    """ Return transitive matrix closure,
    use Warshall’s algorithm to find one

    Args:matrix_size = len(matrix)

    current_matrix = deepcopy(matrix)
    old_matrix = []

    # Dont automatically copy i'th row.
    # This case is being handle by normal row processing.
    for i in range(matrix_size):
        old_matrix = deepcopy(current_matrix)
        for y, row in enumerate(old_matrix):
            # if i'th element of row is 0, copy it to current_matrix
            if row[i] == 0:
                # This row has already been copied in deepcopy()
                continue

            for x, el_ in enumerate(row):
                current_matrix[y][x] = el_ or old_matrix[i][x]

    return current_matrix
        matrix (list[list[int]]): original matrix

    Returns:
        list[list[int]]: transitive closure of matrix

    Examples:
    >>> matrix_transitive_closure([[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    [[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]
    """
    matrix_size = len(matrix)

    current_matrix = deepcopy(matrix)
    old_matrix = []

    # Dont automatically copy i'th row.
    # This case is being handle by normal row processing.
    for i in range(matrix_size):
        old_matrix = deepcopy(current_matrix)
        for y, row in enumerate(old_matrix):
            # if i'th element of row is 0, copy it to current_matrix
            if row[i] == 0:
                # This row has already been copied in deepcopy()
                continue

            for x, el_ in enumerate(row):
                current_matrix[y][x] = el_ or old_matrix[i][x]

    return current_matrix

def is_relation_transitive(matrix: list[list[int]]) -> bool:
    """ Check if matrix is transitive or not

    Args:
        matrix (list[list[int]]): matrix tp check

    Returns:
        bool: True if matrix is transitive, False otherwise

    >>> is_relation_transitive([[1, 1, 0, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]])
    True
    """
    return matrix == matrix_transitive_closure(matrix)

def relation_symmetrical_closure(matrix: list[list[int]]) -> list[list[int]]:
    """ Return matrix of symmetrical closure of given relation 

    Args:
        matrix (list[list[int]]): source matrix

    Returns:
        list[list[int]]: matrix of symmetrical closure
    >>> relation_symmetrical_closure([[1, 0, 0, 1], [0, 1, 0, 1],[1, 1, 0, 1], [0, 0, 0, 0]])
    [[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]

    """
    matrix = deepcopy(matrix)
    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            if el == 1 and matrix[x][y] != 1:
                matrix[x][y] = 1

    return matrix


def relation_reflective_closure(matrix: list[list[int]]) -> list[list[int]]:
    """ Return matrix of reflective closure of given matrix

    Args:
        matrix (list[list[int]]): source matrix

    Returns:
        list[list[int]]: reflective closure matrix
    >>> relation_symmetrical_closure([[0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 0]]
    """
    matrix = deepcopy(matrix)
    n = len(matrix)
    for y in range(n):
        if matrix[y][y] != 1:
            matrix[y][y] = 1

    return matrix

def equivalence_classes(relation: list[list[int]]) -> list[list]:
    """find classes of the equivalence

    Args:
        relation (list[tuple[int]]): relation where the classes shoud be finded

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

def calcualte_transitive_relations(element_source: list[object]) -> int:
    """Calculate number of transitive relations that can be formed
    with given set of elements.

    Args:
        element_source (list[object]): set of elements of relation

    Returns:
        int: number of transitive relations

    Examples:    
    # Go through 65536 4x4 matrix variants and find transitive
    >>> calcualte_transitive_relations([1, 2, 3, 4])
    3994
    """
    transitive_count = 0

    source_size = len(element_source)

    all_matrices = itertools.product([0, 1], repeat=source_size**2)

    for matrix_in_list in all_matrices:
        formated_matrix = [list(matrix_in_list[i*source_size:(i+1)*source_size])
                           for i in range(source_size)]
        transitive_count += is_relation_transitive(formated_matrix)

    return transitive_count


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
