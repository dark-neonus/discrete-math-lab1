import main

matrix, n = main.read_matrix("example.csv")
# for line in matrix:
#     print(line)
main.save_matrix('meow.csv', matrix)
