""" Module to run example for main.py """

import main

FILE_NAME = "test-matrix.csv"

def mark_task(num: int):
    """ Just prints:
    ########## num ##########
    """
    print("#"*10, num, "#"*10)

def run():
    """ Run example script """

    source_matrix = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
    print(f"\n{source_matrix = }")

    mark_task(1)
    print(f"Saving source_matrix to {FILE_NAME}\n")
    main.save_matrix(FILE_NAME, source_matrix)

    matrix, dimension = main.read_matrix(FILE_NAME)
    print(f"Read matrix from {FILE_NAME}")
    print(f"{matrix = } with {dimension = }\n")

    elements = list(range(dimension))
    relation = main.matrix_to_relation(elements, matrix)
    print(f"{relation = } - relation of {matrix = } and {elements = }\n")

    matrix = main.relation_to_matrix(elements, relation)
    print(f"{matrix = } - matrix of {relation = } and {elements = }\n")

    mark_task(2)
    print(f"{matrix = }\nsymmetrical closure\
          {main.relation_symmetrical_closure(matrix)}\n")

    print(f"{matrix = }\nreflective closure\
          {main.relation_reflective_closure(matrix)}\n")

    mark_task(3)
    print(f"{matrix = }\ntransitive closure\
          {main.matrix_transitive_closure(matrix)}\n")

    mark_task(4)
    nice_relation = main.matrix_to_relation(elements,
            main.matrix_transitive_closure(
                main.relation_symmetrical_closure(
                    main.relation_reflective_closure(matrix)
                )
        )
    )
    print(f"{nice_relation = }\nequivalence_classes {main.equivalence_classes(nice_relation)}\n")

    mark_task(5)
    print(f"{matrix = } is transitive: {main.is_relation_transitive(matrix)}\n")

    mark_task(6)
    for i in range(1, 5):
        range_elements = list(range(i))
        print(f"({i}) Number of transitive closure for elements {range_elements}")
        print(main.calcualte_transitive_relations(range_elements))

run()
