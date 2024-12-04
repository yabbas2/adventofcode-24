from utils import *

input_file_path = "./day_04_input.txt"

xmas_mask = [
    ['S', 'O', 'O', 'S', 'O', 'O', 'S'],
    ['O', 'A', 'O', 'A', 'O', 'A', 'O'],
    ['O', 'O', 'M', 'M', 'M', 'O', 'O'],
    ['S', 'A', 'M', 'X', 'M', 'A', 'S'],
    ['O', 'O', 'M', 'M', 'M', 'O', 'O'],
    ['O', 'A', 'O', 'A', 'O', 'A', 'O'],
    ['S', 'O', 'O', 'S', 'O', 'O', 'S'],
]

x_mas_mask_1 = [
    ['M', 'O', 'S'],
    ['O', 'A', 'O'],
    ['M', 'O', 'S'],
]

x_mas_mask_2 = [
    ['S', 'O', 'S'],
    ['O', 'A', 'O'],
    ['M', 'O', 'M'],
]

x_mas_mask_3 = [
    ['M', 'O', 'M'],
    ['O', 'A', 'O'],
    ['S', 'O', 'S'],
]

x_mas_mask_4 = [
    ['S', 'O', 'M'],
    ['O', 'A', 'O'],
    ['S', 'O', 'M'],
]


def apply_xmas_mask(data: str, row_idx: int, col_idx: int) -> int:
    matches = 0
    row_len = len(data[row_idx])
    col_len = len(data)

    # horizontal
    # _0_search
    if (col_idx + 3) < row_len:
        if data[row_idx][col_idx:(col_idx + 4)] == ''.join(xmas_mask[3][3:7]):
            matches += 1
    # _180_search
    if (col_idx - 3) >= 0:
        if data[row_idx][(col_idx - 3):(col_idx + 1)] == ''.join(xmas_mask[3][0:4]):
            matches += 1

    # vertical
    # _270_search
    if (row_idx + 3) < col_len:
        if ''.join([data[row_idx + i][col_idx] for i in range(4)]) == ''.join([xmas_mask[3 + i][3] for i in range(4)]):
            matches += 1
    # _90_search
    if (row_idx - 3) >= 0:
        if ''.join([data[row_idx - i][col_idx] for i in range(4)]) == ''.join([xmas_mask[3 - i][3] for i in range(4)]):
            matches += 1

    # diagonal
    # _45_search
    if (col_idx + 3) < row_len and (row_idx - 3) >= 0:
        if ''.join([data[row_idx - i][col_idx + i] for i in range(4)]) == ''.join([xmas_mask[3 - i][3 + i] for i in range(4)]):
            matches += 1
    # _135_search
    if (col_idx - 3) >= 0 and (row_idx - 3) >= 0:
        if ''.join([data[row_idx - i][col_idx - i] for i in range(4)]) == ''.join([xmas_mask[3 - i][3 - i] for i in range(4)]):
            matches += 1
    # _225_search
    if (col_idx - 3) >= 0 and (row_idx + 3) < col_len:
        if ''.join([data[row_idx + i][col_idx - i] for i in range(4)]) == ''.join([xmas_mask[3 + i][3 - i] for i in range(4)]):
            matches += 1
    # _315_search
    if (col_idx + 3) < row_len and (row_idx + 3) < col_len:
        if ''.join([data[row_idx + i][col_idx + i] for i in range(4)]) == ''.join([xmas_mask[3 + i][3 + i] for i in range(4)]):
            matches += 1

    return matches


def search_xmas(data: str) -> int:
    count = 0
    for row_idx, row in enumerate(data):
        for col_idx in range(len(row)):
            if data[row_idx][col_idx] != 'X':
                continue
            count += apply_xmas_mask(data, row_idx, col_idx)
    return count


def apply_x_mas_mask(data: str, row_idx: int, col_idx: int, x_mas_mask: list) -> int:
    score = 0
    row_len = len(data[row_idx])
    col_len = len(data)

    # diagonal
    # _45_search
    if (col_idx + 1) < row_len and (row_idx - 1) >= 0:
        if data[row_idx - 1][col_idx + 1] == x_mas_mask[0][2]:
            score += 1
    # _135_search
    if (col_idx - 1) >= 0 and (row_idx - 1) >= 0:
        if data[row_idx - 1][col_idx - 1] == x_mas_mask[0][0]:
            score += 1
    # _225_search
    if (col_idx - 1) >= 0 and (row_idx + 1) < col_len:
        if data[row_idx + 1][col_idx - 1] == x_mas_mask[2][0]:
            score += 1
    # _315_search
    if (col_idx + 1) < row_len and (row_idx + 1) < col_len:
        if data[row_idx + 1][col_idx + 1] == x_mas_mask[2][2]:
            score += 1

    return score // 4


def search_x_mas(data: str) -> int:
    count = 0
    for row_idx, row in enumerate(data):
        for col_idx in range(len(row)):
            if data[row_idx][col_idx] != 'A':
                continue
            count += apply_x_mas_mask(data, row_idx, col_idx, x_mas_mask_1)
            count += apply_x_mas_mask(data, row_idx, col_idx, x_mas_mask_2)
            count += apply_x_mas_mask(data, row_idx, col_idx, x_mas_mask_3)
            count += apply_x_mas_mask(data, row_idx, col_idx, x_mas_mask_4)
    return count


if __name__ == "__main__":
    data = read_file_lines(input_file_path)
    count = search_xmas(data)
    print(f"INFO: xmas search count = {count}")
    count = search_x_mas(data)
    print(f"INFO: x-mas search count = {count}")
