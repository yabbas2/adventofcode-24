def read_file_lines(file_path: str) -> list:
    try:
        f = open(file_path, "r")
    except Exception as e:
        print(f"ERROR: expection while opening file: {e}")
    return f.readlines()


def read_file(file_path: str) -> list:
    try:
        f = open(file_path, "r")
    except Exception as e:
        print(f"ERROR: expection while opening file: {e}")
    return f.read()
