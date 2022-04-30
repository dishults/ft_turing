def inverted_color(string):
    return f"\033[;7m{string}\033[0m"


def value_error(field_name, wrong, conditions):
    if wrong:
        wrong = str(wrong)
        if len(wrong) > 80:
            wrong = f"{wrong[:80]}..."
        wrong = f" {inverted_color(wrong)}"
    else:
        wrong = ""
    conditions = "\n - ".join([""] + conditions)
    return (f"{inverted_color(field_name)} has a wrong value{wrong},"
            f" it should respect the following condition(s): {conditions}")


def get_field(machine_description, field):
    try:
        return machine_description[field]
    except KeyError:
        raise AssertionError(
            f"machine description is missing the '{field}' field")
