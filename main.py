
def read_matrix(file_name: str) -> tuple[list[list[int]], int]:
    """Read matrix from file and return it with its dimension.

    Args:
        file_name (str): name of file to open.

    Returns:
        tuple[list[list[int]], int]: tuple of matrix of integer
            from file with given name and dimension of matrix.
    """
    with open(file_name, 'r') as file:
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

    with open(file_name, "w") as file:
        text = ''
        for line in matrix:
            row = ''
            for el in line:
                row += str(el)
            text += row + '\n'
        file.write(text[:-1])

