def selection_sort(array):
    length = len(array)
    for i in range(length - 1):
        mn_ind = i
        for j in range(i + 1, length):
            if array[mn_ind] > array[j]:
                mn_ind = j
        if mn_ind != i:
            array[i], array[mn_ind] = array[mn_ind], array[i]
    return array
def main():
    array = [5, 3, 8, 1, -5, 6]
    print(selection_sort(array))

if __name__ == '__main__':
    main()
