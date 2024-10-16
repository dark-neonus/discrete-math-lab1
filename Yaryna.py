def relation_symmetrical_closure(matrix: list[list[int]]) -> list[list[int]]:
    """_summary_

    Args:
        matrix (list[list[int]]): _description_

    Returns:
        list[list[int]]: _description_
    >>> relation_symmetrical_closure([[1, 0, 0, 1], [0, 1, 0, 1],[1, 1, 0, 1], [0, 0, 0, 0]])
    [[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]

    """
   
    
  
    
    
    for y, row in enumerate(matrix):
        for x, el in enumerate(row):
            if el == 1 and matrix[x][y] != 1:
                matrix[x][y] = 1

    return matrix


def relation_reflective_closure(matrix: list[list[int]]) -> list[list[int]]: 
    """_summary_

    Args:
        matrix (list[list[int]]): _description_

    Returns:
        list[list[int]]: _description_
    >>> relation_symmetrical_closure([[0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 0]]
    """
    n = len(matrix)
    for y in range(n):
        if matrix[y][y] != 1:
            matrix[y][y] = 1

    return matrix

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
