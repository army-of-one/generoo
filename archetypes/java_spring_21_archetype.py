from pystache import Renderer

from archetypes.archetype import Archetype
import os
from utils import *


class JavaSpring21Archetype(Archetype):

    # Defaults
    default_group_id = "tech.armyofone"
    default_artifact_id = "test"

    # Constants
    maven_source_path = 'src/main/java'
    maven_resource_path = 'src/main/resources'
    maven_test_source_path = 'src/test/java'
    maven_test_resource_path = 'src/test/resources'

    template_path = 'archetypes/templates/java/spring-boot/2.1'

    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def generate_project(self):
        group_id = prompt_for_input("Group ID:", default=self.default_group_id)
        artifact_id = prompt_for_input("Artifact ID:", default=self.default_artifact_id)
        self.generate_api_package(group_id, artifact_id)

    def generate_resource(self):
        super(JavaSpring21Archetype, self).generate_resource()

    def copy_api_files(self, group_id, artifact_id, module_name, source_path):
        parameters = {
            'artifact_id': artifact_id,
            'group_id': group_id,
            'capital_case_artifact_id': convert_to_caps_no_spaces(artifact_id),
            'period_artifact_id': convert_to_period_case(artifact_id)
        }
        self.write_template_to_directory(f'{module_name}/pom.xml', f'{self.template_path}/$api$pom.xml', parameters)
        self.write_template_to_directory(f'{source_path}/{convert_to_caps_no_spaces(artifact_id)}Controller.java',
                                    f'{self.template_path}/$artifact_id$Controller.java', parameters)
        self.write_template_to_directory(f'{source_path}/Application.java', f'{self.template_path}/Application.java', parameters)

    def write_template_to_directory(self, file: str, template: str, parameters: dict):
        f = open(file, 'w')
        f.write(self.renderer.render(open(template, 'r').read(), parameters))
        f.close()

    def generate_api_package(self, group_id: str, artifact_id: str):
        module_name = f'{artifact_id}-api'
        source_path, test_source_path, resource_path, test_resource_path = self.generate_maven_package_structure(group_id, module_name)
        self.copy_api_files(group_id, artifact_id, module_name, source_path)

    def generate_maven_package_structure(self, group_id: object, module_name: object) -> object:
        period_module_name = convert_to_period_case(module_name)
        full_package = f'{group_id}.{period_module_name}'
        full_path = package_to_file(full_package)
        source_path = f'{module_name}/{self.maven_source_path}/{full_path}'
        test_source_path = f'{module_name}/{self.maven_test_source_path}/{full_path}'
        resource_path = f'{module_name}/{self.maven_resource_path}'
        test_resource_path = f'{module_name}/{self.maven_test_resource_path}'
        os.makedirs(source_path)
        os.makedirs(test_source_path)
        os.makedirs(resource_path)
        os.makedirs(test_resource_path)
        return source_path, test_source_path, resource_path, test_resource_path

