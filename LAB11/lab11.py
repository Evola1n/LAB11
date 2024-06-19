def sum_of_squares(arr):
    return sum(x ** 2 for x in arr)


def filter_and_sum(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)

from collections import Counter

def sort_by_frequency(arr):
    freq = Counter(arr)
    arr.sort(key=lambda x: (-freq[x], x))
    return arr


def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)



def longest_consecutive(arr):
    if not arr:
        return 0
    arr = set(arr)
    longest_streak = 0

    for num in arr:
        if num - 1 not in arr:
            current_num = num
            current_streak = 1

            while current_num + 1 in arr:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak



def rotate_array(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]


def array_of_products(arr):
    length = len(arr)
    left_products = [1] * length
    right_products = [1] * length
    result = [1] * length

    for i in range(1, length):
        left_products[i] = left_products[i - 1] * arr[i - 1]

    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * arr[i + 1]

    for i in range(length):
        result[i] = left_products[i] * right_products[i]

    return result



def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum



def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result



import heapq

def k_closest_points(points, k):
    return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)

