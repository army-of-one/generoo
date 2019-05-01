from os.path import dirname, basename, isfile, join
import glob

before_file_extension = -len(".py")

modules = glob.glob(join(dirname(__file__), "*.py"))

__all__ = [basename(f)[:before_file_extension] for f in modules if isfile(f) and not f.endswith('__init__.py')]
