import abc


class Archetype:
    """
    Archetypes represent a combination of language, framework, and version. Each generator for this project will inherit
    from an archetype to ensure that generation is done in a consistent and repeatable way.

    Since the scope of generation can vary, from the project level to the resource level, this interface will offer
    varying degrees of scope. If, for some reason, generation on any scope can not be complete, then a not implemented
    exception should be raised.
    """

    @abc.abstractmethod
    def generate_project(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def generate_resource(self, **kwargs):
        raise NotImplementedError
