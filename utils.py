def convert_to_hyphen_case(string):
    return str.replace(string, '.', '-')


def convert_to_caps_with_spaces(string):
    return str.replace(string, '-', ' ').capitalize()


def convert_to_caps_no_spaces(string):
    return str.replace(string, '-', ' ').capitalize()


def convert_to_period_case(string):
    return str.replace(string, '-', '.')


def package_to_file(string):
    return str.replace(string, '.', '/')


def prompt_for_input(prompt, default: str = "", options=None):
    if options is None:
        options = []
    prompt_text = prompt
    if default is not "":
        prompt_text += f"({default})"
    if len(options) > 0:
        prompt_text += f"[{options}]"
    prompt_text += ": "
    input_response = input(prompt_text)
    if input_response is "":
        input_response = default
    return input_response