import os
import pystache

# Options
yes_no = ['yes', 'YES', 'Yes', 'y', 'Y', 'N', 'n', 'no', 'No', 'NO']
database_options = ['none', 'postgres']

# Defaults
default_group_id = "tech.armyofone"
default_artifact_id = "test"

# Constants
maven_source_path = 'src/main/java'
maven_resource_path = 'src/main/resources'

maven_test_source_path = 'src/test/java'
maven_test_resource_path = 'src/test/resources'


def prompt_user():
    database = prompt_for_input("Enter the type of database this application needs", default='none', options=database_options)
    while database not in database_options:
        database = prompt_for_input("Enter the type of database this application needs", default='none', options=database_options)
    if database is not 'none':
        prompt_db()


def prompt_db():
    print('\n\n\nSKELETON FUNCTIONALITY\n\n\n')
    url = prompt_for_input("Enter JDBC URL for DB")
    print(url)


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


def generate_base_packages():
    group_id = prompt_for_input("Group ID:", default=default_group_id)
    artifact_id = prompt_for_input("Artifact ID:", default=default_artifact_id)
    generate_api_package(group_id, artifact_id)


def copy_api_files(group_id, artifact_id, module_name, source_path, test_source_path, resource_path,
                   test_resource_path):
    parameters = {
        'artifact_id': artifact_id,
        'group_id': group_id,
        'capital_case_artifact_id': convert_to_caps_no_spaces(artifact_id),
        'period_artifact_id': convert_to_period_case(artifact_id)
    }
    write_template_to_directory(f'{module_name}/pom.xml', 'templates/$api$pom.xml', parameters)
    write_template_to_directory(f'{source_path}/{convert_to_caps_no_spaces(artifact_id)}Controller.java', 'templates/{{artifact_id}}Controller.java', parameters)
    write_template_to_directory(f'{source_path}/Application.java', 'templates/Application.java', parameters)


def write_template_to_directory(file: str, template: str, parameters: dict):
    f = open(file, 'w')
    f.write(renderer.render(open(template, 'r').read(), parameters))
    f.close()


def generate_api_package(group_id: str, artifact_id: str):
    module_name = f'{artifact_id}-api'
    source_path, test_source_path, resource_path, test_resource_path = generate_maven_package_structure(group_id, module_name)
    copy_api_files(group_id, artifact_id, module_name, source_path, test_source_path, resource_path, test_resource_path)


def generate_maven_package_structure(group_id: str, module_name: str):
    period_module_name = convert_to_period_case(module_name)
    full_package = f'{group_id}.{period_module_name}'
    full_path = package_to_file(full_package)
    source_path = f'{module_name}/{maven_source_path}/{full_path}'
    test_source_path = f'{module_name}/{maven_test_source_path}/{full_path}'
    resource_path = f'{module_name}/{maven_resource_path}'
    test_resource_path = f'{module_name}/{maven_test_resource_path}'
    os.makedirs(source_path)
    os.makedirs(test_source_path)
    os.makedirs(resource_path)
    os.makedirs(test_resource_path)
    return source_path, test_source_path, resource_path, test_resource_path


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


renderer = pystache.Renderer()
generate_base_packages()
