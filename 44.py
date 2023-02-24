def quicksort(input_list: list[int], low: int, high: int) -> None:
    if low < high:
        pivot_idx = partition(input_list, low, high)
        quicksort(input_list, low, pivot_idx - 1)
        quicksort(input_list, pivot_idx + 1, high)


def partition(input_list: list[int], low: int, high: int) -> int:
    pivot = input_list[high]
    pivot_idx = low - 1
    for current_idx in range(low, high):
        if input_list[current_idx] <= pivot:
            pivot_idx = pivot_idx + 1
            input_list[pivot_idx], input_list[current_idx] = input_list[current_idx], input_list[pivot_idx]
    input_list[pivot_idx + 1], input_list[high] = input_list[high], input_list[pivot_idx + 1]
    return pivot_idx + 1


arr = [5, 7, 8, 1, 2, 4, 99, 77, 56, 43, 12, 98]
quicksort(arr, 0, len(arr) - 1)

print(arr)
