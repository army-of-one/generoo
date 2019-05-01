from pystache import Renderer

from archetypes.java_spring_21_archetype import JavaSpring21Archetype

renderer = Renderer()


def generate_archetype(language: str, framework: str, version: str):
    if language == 'java':
        if framework == 'spring-boot':
            if version == '2.1':
                return JavaSpring21Archetype(renderer)




