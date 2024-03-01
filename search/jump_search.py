def jump_search(array, el):
    length = len(array)
    jump = int(length ** 0.5)
    left = 0
    while left < length and array[left] <= el:
        right = min(length - 1, left + jump)
        if array[left] <= el <= array[right]:
            break

        left += jump
    else:
        return -1

    for i in range(left, right + 1):
        if array[i] == el:
            return i
    return -1

def main():
    array = [-5, -2, 0, 4, 100]
    array.sort()
    result = jump_search(array, 4)
    if result != -1:
        print(f"Element in array. His index: {result}")
    else:
        print("Element not in array")

if __name__ == '__main__':
    main()
