#! python3



def load_data(path):
    matrix = list()
    with open(path, "r") as f:
        size = f.readline().replace("\n", "").replace("\t", " ")
        print(f"> now is {size} x {size}'s matrix.\n")
        for line in f.readlines():
            split_data = line.replace("\n", "").replace("\t", "").split(" ")
            temp = list(int(i) for i in split_data)
            matrix.append(temp)
    return matrix


def shortest_path(matrix, v, n, o):
    path = list()
    if (v[n] == 1 or n == o):
        return path
    else:
        v[n] = 1

    point = list()
    for index in range(len(matrix)):
        if (index == o and matrix[n][index] == 1):
            return [[n, o]]
        if (matrix[n][index] == 1 and v[index] == 0):
            point.append(index)

    for p in point:
        if (matrix[p][o] == 1):
            path.append([p, o])
    
    if (len(path) == 0):
        for p in point:
            path += shortest_path(matrix, v, p, o)
    
    if (len(path) != 0):
        for index in range(len(path)):
            path[index].insert(0, n)
    return path


#show matrix
def show(matrix):
    print("    ", end="")
    for index in range(len(matrix)):
        print(f"{index}  ", end="")
    print()
    for index in range(len(matrix)):
        print(f"{index:2} {matrix[index]}")


def main():
    matrix = load_data("data.txt")

    show(matrix)

    test_point = [(0, 1), (1, 3), (0, 3)]
    
    print("\n")

    for point in test_point:
        print(f"{point[0]}->{point[1]}:", end="")
        print(shortest_path(matrix, list(0 for _ in range(len(matrix))), point[0], point[1]))


if (__name__ == "__main__"):
    main()
    input("press key of enter to continue...")