import main

# for i in range(1, 6):
#     print(i, main.calcualte_transitive_relations(list(range(i))))

import time

start_time = time.time()

result = main.calcualte_transitive_relations(list(range(4)))

end_time = time.time()

time_for_one_matrix_4 = (end_time - start_time) / (2**16)

print(f"time_taken: {end_time - start_time}\n{time_for_one_matrix_4 = }")

import itertools

transitive_count = 0
element_source = list(range(5))

source_size = len(element_source)

all_matrices = itertools.product([0, 1], repeat=source_size**2)

i = 0

start_time = time.time()
for matrix in all_matrices:
    formated_matrix = [list(matrix[i:i+source_size]) for i in range(source_size)]
    transitive_count += main.is_relation_transitive(formated_matrix)
    if i == 10000:
        i = i % 10000
        end_time = time.time()
        start_time = time.time()



