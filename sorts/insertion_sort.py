def insertion_sort(array):
    length = len(array)
    for i in range(1, length):
        sorted = i - 1
        while sorted > -1 and array[sorted] > array[sorted + 1]:
            array[sorted], array[sorted + 1] = array[sorted + 1], array[sorted]
            sorted -= 1
    return array
def main():
    array = [5, 3, 8, 1, -5, 6]
    print(insertion_sort(array))

if __name__ == '__main__':
    main()