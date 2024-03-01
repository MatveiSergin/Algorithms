def partOfSort(array, left, right):
    m = array[(left + right) // 2]
    while left <= right:
        while array[left] < m:
            left += 1
        while array[right] > m:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left
def recursion_quick_sort(array, start, end):
    if start >= end:
        return array
    right_start = partOfSort(array, start, end)
    recursion_quick_sort(array, start, right_start - 1)
    return recursion_quick_sort(array, right_start, end)
def quick_sort(array):
    sort_array = recursion_quick_sort(array, 0, len(array) - 1)
    return sort_array
def main():
    array = [5, 3, 8, 1, -5, 6]
    print(quick_sort(array))

if __name__ == '__main__':
    main()