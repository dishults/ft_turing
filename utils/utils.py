import os


def strigify_array(array, sep=', ', padding=' '):
    return f"[{padding}{sep.join(array)}{padding}]"


def wrap_string(string, columns, outer='*', inner=' '):
    def outer_line():
        return outer * columns

    def inner_line():
        return f"{outer}{inner * (columns - 2)}{outer}"

    free_space = max(0, (columns - len(string)) // 2)
    string = f"{outer}{inner * (free_space - 1)}{string}{inner * (free_space - 1)}{outer}"
    if len(string) < columns:
        string = f"{string[:-1]}{inner * (columns - len(string))}{outer}"

    return "\n".join([outer_line(), inner_line(), string, inner_line(), outer_line()])


def highlight(string):
    return f"\033[;7m{string}\033[0m"


def value_error(field_name, wrong, conditions):
    if wrong:
        wrong = str(wrong)
        if len(wrong) > 80:
            wrong = f"{wrong[:80]}..."
        wrong = f" {highlight(wrong)}"
    else:
        wrong = ""
    conditions = "\n - ".join([""] + conditions)
    return (f"{highlight(field_name)} has a wrong value{wrong},"
            f" it should respect the following condition(s): {conditions}")


def get_field(machine_description, field):
    try:
        return machine_description[field]
    except KeyError:
        raise AssertionError(
            f"machine description is missing the '{field}' field")


def get_terminal_size():
    try:
        return os.get_terminal_size()
    except Exception:
        return [80, 24]


def get_file_name(file_path):
    return os.path.basename(file_path).split('.json')[0]
