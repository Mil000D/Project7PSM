import numpy as np
import matplotlib.pyplot as plt


# Function that carry out all necessary calculations
# to return matrix of temperature distribution
# (it also prints values stored in that matrix,
# so they can be easily transferred to Excel for example)
def calculations() -> list:
    list_of_coordinates = []
    min_row_or_col = 0
    max_row = 41
    max_col = 41
    for j in range(1, 41):
        for i in range(1, 41):
            list_of_coordinates.append((i, j))

    list_ = [[(elem[0] + 1, elem[1]), (elem[0], elem[1]), (elem[0] - 1, elem[1]), (elem[0], elem[1] + 1),
              (elem[0], elem[1] - 1)] for elem in list_of_coordinates]

    matrix = []

    for i, elem1 in enumerate(list_):
        list_of_values = []
        for elem2 in list_of_coordinates:
            if elem2 == list_of_coordinates[i]:
                list_of_values.append(-4)
            else:
                list_of_values.append(elem1.count(elem2))
        matrix.append(list_of_values)

    output = []
    for elem1 in list_:
        result = 0
        for elem2 in elem1:
            if elem2[1] == min_row_or_col:
                result -= 150
            elif elem2[1] == max_row:
                result -= 200
            elif elem2[0] == min_row_or_col:
                result -= 100
            elif elem2[0] == max_col:
                result -= 50
        output.append(result)

    matrix = np.array(matrix)
    matrix_inverse = np.linalg.inv(matrix)

    matrix_inverse = np.array(matrix_inverse)
    output = np.array(output)
    dot_product = matrix_inverse.dot(output)

    matrix = []
    for i in reversed(range(0, len(dot_product), 40)):
        list_ = []
        for j in range(i, i + 40):
            if j < len(dot_product):
                list_.append(dot_product[j])
                print(str(dot_product[j]).replace(".", ","), end=" ")
        matrix.append(list_)
        print()

    return matrix


# Function that displays plot for given matrix
def display_plot(matrix: list) -> None:
    matrix = np.array(matrix)
    min_val = 50
    max_val = 200

    cmap = plt.get_cmap('RdYlGn_r')

    normalize = plt.Normalize(min_val, max_val)

    _, ax = plt.subplots()
    im = ax.imshow(matrix, cmap=cmap, norm=normalize)

    ax.figure.colorbar(im, ax=ax)

    plt.show()


# All calculations are done for n = 41,
# so the output matrix will be 40x40
matrix_ = calculations()
display_plot(matrix_)
