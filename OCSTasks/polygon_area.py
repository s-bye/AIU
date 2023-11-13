def calculate_area(x, y, n):
    polygon_area = 0.0
    j = n - 1
    for i in range(0, n):
        polygon_area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return abs(polygon_area / 2.0)


def main():
    n = int(input("Enter the number of vertices in the polygon: "))
    x = []
    y = []
    print('Enter the x and y coordinates separated by a space, for example: 2 4 or -5 7')

    for i in range(n):
        x_coordinate, y_coordinate = map(int, input("Enter the coordinates of vertex {}: ".format(i + 1)).split())
        x.append(x_coordinate)
        y.append(y_coordinate)

    polygon_area = calculate_area(x, y, n)
    print("The area of the polygon is:", polygon_area)


if __name__ == "__main__":
    main()
