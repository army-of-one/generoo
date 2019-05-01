import argparse
import os
import json
from pick import pick

from utils import prompt_for_input, convert_to_hyphen_case, package_to_file, convert_to_period_case, \
    convert_to_caps_no_spaces, convert_to_caps_with_spaces

yes_no = ['yes', 'YES', 'Yes', 'y', 'Y', 'N', 'n', 'no', 'No', 'NO']
generate_options = ['generate', 'gen', 'g']
project_options = ['project', 'proj', 'pro', 'p']


database_options = ['none', 'postgres']

excluded_archetypal_directories = ['common']


def create_configuration_directory(args: argparse.Namespace, run_configuration: dict):
    """
    When new projects are created, Generoo will add a configuration file to the root directory of the project. This
    configuration file can be used to prepopulate date in subsequent generoo generation tasks. See documentation on
    github for more information.
    """
    print('Creating generoo configuration directory...')
    generoo_directory = f'{args.name}/.generoo'
    try:
        os.makedirs(generoo_directory)
    except FileExistsError:
        print('Generoo configuration directory already exists.')
    run_configuration_file = open(f'{generoo_directory}/run-configuration.json', 'w')
    run_configuration_file.write(json.dumps(run_configuration, indent=4, sort_keys=True))
    run_configuration_file.close()
    print('Successfully created generoo configuration directory.')


def prompt_for_archetype():
    language, _ = pick(get_languages(), "Please choose a language:")
    framework, _ = pick(get_framework(language), "Please choose a framework:")
    version, _ = pick(get_versions(language, framework), "Please choose a version:")
    return language, framework, version


def get_languages():
    """Traverse templates directory to pull out all of the directories that represent languages. Ignore common.py."""
    root = 'archetypes/templates'
    return [subdirectory for subdirectory in os.listdir(root) if os.path.isdir(os.path.join(root, subdirectory))
            and subdirectory not in excluded_archetypal_directories]


def get_framework(language: str):
    """
    Traverse templates/{language} directory to pull out all of the directories that represent archetypes.
    Ignore common.py.
    """
    root = f'archetypes/templates/{language}'
    return [subdirectory for subdirectory in os.listdir(root) if os.path.isdir(os.path.join(root, subdirectory))
            and subdirectory not in excluded_archetypal_directories]


def get_versions(language: str, framework: str):
    """
    Traverse templates/{language}/{framework} directory to pull out all of the directories that represent versions.
    Ignore common.py.
    """
    root = f'archetypes/templates/{language}/{framework}'
    return [subdirectory for subdirectory in os.listdir(root) if os.path.isdir(os.path.join(root, subdirectory))
            and subdirectory not in excluded_archetypal_directories]


def get_generoo_config(args: argparse.Namespace) -> dict:
    configuration = open(f'{args.name}/run-configuration.json')
    return json.loads(configuration)


def get_template_config(args: argparse.Namespace) -> str:
    if args.template_config:
        path = args.template_config
    else:
        language, framework, version = prompt_for_archetype()
        path = f'archetypes/templates/{language}/{framework}/{version}/template-config.json'
    return path


def resolve_variables(template_configuration: dict) -> dict:
    """
    The first step of the lifecycle is to collect the variables provided in the configuration.

    This will add the name and value of each variable to the run-configuration.

    :param template_configuration:
    :return:
    """
    run_configuration = {}
    variables = template_configuration['variables']
    if variables:
        for variable in variables:
            if variable['name']:
                run_configuration[variable['name']] = variable['value']
            else:
                raise AttributeError
    return run_configuration


def resolve_prompts(run_configuration: dict, template_configuration: dict) -> dict:
    """
    The second step of the lifecycle is to collect the user inputs via the prompts. The values will also be written to
    the run configuration.

    :param run_configuration:
    :param template_configuration:
    :return:
    """
    prompts = template_configuration['prompts']
    if prompts:
        for prompt in prompts:
            if prompt['name'] and prompt['text']:
                default = prompt.get('default')
                options = prompt.get('options')
                value = prompt_for_input(prompt['text'], default=default, options=options)
                run_configuration[prompt['name']] = value
            else:
                raise AttributeError
    return run_configuration


def resolve_transformations(run_configuration: dict, template_configurations: dict) -> dict:
    """
    The third step of the lifecycle is to make the desired transformations. The values will also be written to the run
    configuration.

    :param run_configuration:
    :param template_configurations:
    :return:
    """
    transformations = template_configurations['transformations']
    if transformations:
        for transformation in transformations:
            name = transformation['name']
            reference = transformation['reference']
            transformation_type = transformation['transformation']
            if name and reference and transformation:
                if transformation_type == 'DASHES':
                    run_configuration[name] = convert_to_hyphen_case(run_configuration[reference])
                if transformation_type == 'SLASHES':
                    run_configuration[name] = package_to_file(run_configuration[reference])
                if transformation_type == 'PERIODS':
                    run_configuration[name] = convert_to_period_case(run_configuration[reference])
                if transformation_type == 'CAPITALIZED':
                    run_configuration[name] = convert_to_caps_no_spaces(run_configuration[reference])
                if transformation_type == 'CAPITALIZED_WITH_SPACES':
                    run_configuration[name] = convert_to_caps_with_spaces(run_configuration[reference])
            else:
                raise AttributeError
    return run_configuration


def resolve_template_configuration(template_configuration: dict) -> dict:
    """
    Runs the lifecycle events for loading the template file. Returns a run configuration.

    :param template_configuration:
    :return:
    """
    run_configuration = resolve_variables(template_configuration)
    run_configuration = resolve_prompts(run_configuration, template_configuration)
    run_configuration = resolve_transformations(run_configuration, template_configuration)
    return run_configuration


def generate_project(args: argparse.Namespace):
    try:
        run_configuration = get_generoo_config(args)
    except IOError:
        print('No pre-existing generoo run configuration found...')
        raw_configuration = open(get_template_config(args))
        configuration = json.loads(raw_configuration.read())
        raw_configuration.close()
        run_configuration = resolve_template_configuration(configuration)
        create_configuration_directory(args, run_configuration)
    print(run_configuration)


def run(args: argparse.Namespace):
    if args.goal in generate_options:
        if args.scope in project_options:
            generate_project(args)


parser = argparse.ArgumentParser(description='Generate code from templates.')

# Positional Arguments
parser.add_argument('goal', help='A generator goal. Examples: generate, config')
parser.add_argument('scope', help='A generator scope. Examples: project, resource')
parser.add_argument('name', help='The name for the scope. Example: test, pet, inventory')

# Keyword Arguments
parser.add_argument('-n', '--no-config',
                    help='Will run generoo without a pre-existing configuration.')
parser.add_argument('-a', '--auto-config',
                    help='Will run generoo using the pre-existing configuration '
                         'and only prompting for values not present in the configuration.')
parser.add_argument('-c', '--template-config',
                    help='Points to a location on the system that contains a custom template config.')
parser.add_argument('-t', '--templates',
                    help='Points to a directory on the system that contains templates for a corresponding '
                         'template config')

args = parser.parse_args()
run(args)
