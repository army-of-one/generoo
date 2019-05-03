import os
import regex
from pystache import Renderer

# TODO: implement the proper RegEx for the convert methods. Only work from '-' right now
yes_no = ['yes', 'YES', 'Yes', 'y', 'Y', 'N', 'n', 'no', 'No', 'NO']


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


def handle_prompt(prompt: dict):
    prompt_type = prompt.get('type')
    if not prompt_type:
        prompt_type = 'STRING'
    if prompt_type == 'BOOL':
        prompt['options'] = yes_no
    return prompt_user(prompt)


def prompt_user(prompt: dict):
    text = prompt['text']
    default = prompt.get('default')
    options = prompt.get('options')
    validations = prompt.get('validations')
    text = format_prompt_text(text, default, options)
    input_response = input(text)
    if input_response is "":
        input_response = default
    valid = is_valid_input(input_response, validations)
    while not valid:
        text = f'{text[0:-2]} ({get_validation_strings(validations)}): '
        input_response = input(text)
        valid = is_valid_input(input_response, validations)
    return input_response


def format_prompt_text(text, default, options):
    if default is not None and not "":
        text += f"({default})"
    if options is not None and len(options) > 0:
        text += f"[{options}]"
    text += ": "
    return text


def get_validation_strings(validations: list) -> str:
    validation_string = "The following validations must be met to continue: "
    for validation in validations:
        evaluation = validation['evaluation']
        value = validation['value']
        if evaluation:
            if evaluation == 'REGEX':
                text = f'Must match regular expression: {value}. '
            elif evaluation == 'GREATER_THAN':
                text = f'Must be greater than: {value}. '
            elif evaluation == 'LESS_THAN':
                text = f'Must be less than: {value}. '
            else:
                raise AttributeError(f'Invalid evaluation type for validations: {evaluation}')
            validation_string += text
    return validation_string[:-1]


def yes_no_to_bool(input: str):
    return yes_no.index(input) < len(yes_no)/2


def is_valid_input(input_response: str, validations: list) -> bool:
    """
    Will compare for valid input against a user response.

    At the moment, using the greater than or less than comparator is only support for integer types.

    :param input_response:
    :param validations:
    :return:
    """
    valid = True
    if validations:
        for validation in validations:
            evaluation = validation['evaluation']
            value = validation['value']
            if evaluation:
                if evaluation == 'REGEX':
                    valid = regex.match(value, input_response)
                elif evaluation == 'GREATER_THAN':
                    valid = int(input_response) > value
                elif evaluation == 'LESS_THAN':
                    valid = int(input_response) < value
                elif evaluation == 'BOOL':
                    valid = yes_no_to_bool(input_response) == value
                else:
                    raise AttributeError(f'Invalid evaluation type for validations: {evaluation}')
                if not valid:
                    return valid
    return valid


renderer = Renderer()
