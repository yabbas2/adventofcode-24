from utils import read_file_lines

input_file_path = "./day_01_input.txt"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def get_total_distance(left, right):
    total_distance = 0

    assert len(left) == len(right), "ERROR: Lists with different length"
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    return total_distance


def binary_search(arr, val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == val:
            return mid

        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


count_map = {}


def get_binary_search_count(arr, val):
    if val in count_map:
        return count_map[val]

    idx = binary_search(arr, val)
    if idx == -1:  # not found
        count_map[val] = 0
        return 0
    # else: at least found once
    count = 1

    # check similar numbers around idx
    r_idx = idx + 1
    while r_idx < len(arr) and arr[r_idx] == val:
        count += 1
        r_idx += 1
    l_idx = idx - 1
    while l_idx >= 0 and arr[l_idx] == val:
        count += 1
        l_idx -= 1

    count_map[val] = count
    return count


def get_similarity_score(left, right):
    total_sim_score = 0

    for num in left:
        total_sim_score += num * get_binary_search_count(right, num)

    return total_sim_score


def convert_lines_to_lists(lines, left_list, right_list):
    for line in lines:
        line = list(map(int, line.split("   ")))
        left_list.append(line[0])
        right_list.append(line[1])


if __name__ == "__main__":
    # form left and right lists
    left_list = list()
    right_list = list()
    file_lines = read_file_lines(input_file_path)
    convert_lines_to_lists(file_lines, left_list, right_list)
    # start algorithm
    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)
    total_distance = get_total_distance(sorted_left_list, sorted_right_list)
    print(f"INFO: total distance: {total_distance}")
    total_sim_score = get_similarity_score(sorted_left_list, sorted_right_list)
    print(f"INFO: total similarity score: {total_sim_score}")
