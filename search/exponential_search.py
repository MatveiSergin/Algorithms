from search.binary_search import binary_search


def exponential_search(array, el):
    if array[0] == el:
        return 0
    ind = 1
    while ind < len(array) and array[ind] <= el:
        ind *= 2

    return binary_search(array[:min(len(array), ind)], el)

def main():
    array = [-5, -2, 0, 4, 100]
    array.sort()
    result = exponential_search(array, 4)
    if result != -1:
        print(f"Element in array. His index: {result}")
    else:
        print("Element not in array")

if __name__ == '__main__':
    main()