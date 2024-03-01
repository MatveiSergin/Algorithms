def binary_search(array, el):
    start = 0
    end = len(array) - 1
    ind = -1

    while start <= end and ind == -1:
        middle_ind = (start + end) // 2
        middle_el = array[middle_ind]

        if middle_el == el:
            ind = middle_ind

        if middle_el > el:
            end = middle_ind - 1
        else:
            start = middle_ind + 1
    return ind

def main():
    array = [-5, -2, 0, 4, 100]
    array.sort()
    result = binary_search(array, 0)
    if result != -1:
        print(f"Element in array. His index: {result}")
    else:
        print("Element not in array")

if __name__ == '__main__':
    main()