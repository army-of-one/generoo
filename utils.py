import os
from pystache import Renderer

# TODO: implement the proper RegEx for the convert methods. Only work from '-' right now


def convert_to_hyphen_case(string):
    return str.replace(string, '.', '-')


def convert_to_caps_with_spaces(string):
    words = string.split('-')
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return str.join(' ', capitalized_words)


def convert_to_caps_no_spaces(string):
    words = string.split('-')
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return str.join('', capitalized_words)


def convert_to_period_case(string):
    return str.replace(string, '-', '.')


# '[-/\\_]\s'
def package_to_file(string):
    return str.replace(string, '-', '/')


def render_template_to_directory(destination: str, template: str, parameters: dict):
    overwrite_file(destination, renderer.render(open(template, 'r').read(), parameters))


def render_destination_path(destination: str, parameters: dict) -> str:
    return renderer.render(destination, parameters)


def overwrite_file(file, content):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    f = open(file, 'w')
    f.write(content)
    f.close()


def prompt_for_input(prompt, default: str = "", options=None):
    if options is None:
        options = []
    prompt_text = prompt
    if default is not None and not "":
        prompt_text += f"({default})"
    if len(options) > 0:
        prompt_text += f"[{options}]"
    prompt_text += ": "
    input_response = input(prompt_text)
    if input_response is "":
        input_response = default
    return input_response


renderer = Renderer()
