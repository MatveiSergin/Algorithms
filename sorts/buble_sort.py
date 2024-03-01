def buble_sort(array):
    length = len(array)
    while length != 0:
        mx_ind = 0
        for i in range(length - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                mx_ind = i + 1
        length = mx_ind
    return array

def main():
    array = [5, 3, 8, 1, -5, 6]
    print(buble_sort(array))

if __name__ == '__main__':
    main()