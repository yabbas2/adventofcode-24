import re
from utils import *

input_file_path = "./day_03_input.txt"


def get_sum_of_mul_instructions(mul_pattern: re.Pattern, memory: str) -> int:
    sum = 0
    for match in mul_pattern.finditer(memory):
        # some valiation checks
        assert match.group(1).startswith("mul(") and match.group(1).endswith(")"), f"{match.group(1)} does not contain mul()"
        assert int(match.group(2), 10) < 1000 and int(match.group(2), 10) >= 0, f"{match.group(1)} does not contain valid number 1"
        assert int(match.group(3), 10) < 1000 and int(match.group(3), 10) >= 0, f"{match.group(1)} does not contain valid number 2"
        # result
        sum += int(match.group(2), 10) * int(match.group(3), 10)
    return sum


def filter_memory(do_pattern: re.Pattern, dont_pattern: re.Pattern, memory: str) -> str:
    dont_pos = [match.start(1) for match in dont_pattern.finditer(memory)]
    if len(dont_pos) == 0:
        return memory
    do_pos = [match.start(1) for match in do_pattern.finditer(memory)]
    for i in dont_pos:
        for j in do_pos:
            if i < j:
                return filter_memory(do_pattern, dont_pattern, memory[:i] + memory[j:])


if __name__ == "__main__":
    mul_pattern = re.compile(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))")
    do_pattern = re.compile(r"(do\(\))")
    dont_pattern = re.compile(r"(don't\(\))")

    memory = read_file(input_file_path)

    filtered_memory = filter_memory(do_pattern, dont_pattern, memory)

    result = get_sum_of_mul_instructions(mul_pattern, filtered_memory)
    print(f"INFO: sum = {result}")
