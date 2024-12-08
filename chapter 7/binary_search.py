def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

sorted_numbers = [1, 2, 3, 4, 5, 6, 7]
index_of_four = binary_search(sorted_numbers, 4)
print(index_of_four)

index_of_eight = binary_search(sorted_numbers, 8)
print(index_of_eight)

assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0
assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1
assert binary_search([], 1) == -1  # Пустой массив
print("Все тесты пройдены!")
