import pystache
import os
from pick import pick

# Options
from archetypes.archetype_factory import generate_archetype

yes_no = ['yes', 'YES', 'Yes', 'y', 'Y', 'N', 'n', 'no', 'No', 'NO']
database_options = ['none', 'postgres']

excluded_archetypal_directories = ['common']


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


def get_versions(language: str, archetype: str):
    """
    Traverse templates/{language}/{archetype} directory to pull out all of the directories that represent versions.
    Ignore common.py.
    """
    root = f'archetypes/templates/{language}/{archetype}'
    return [subdirectory for subdirectory in os.listdir(root) if os.path.isdir(os.path.join(root, subdirectory))
            and subdirectory not in excluded_archetypal_directories]


language, framework, version = prompt_for_archetype()
generator = generate_archetype(language, framework, version)
generator.generate_project()
# generate_base_packages()
