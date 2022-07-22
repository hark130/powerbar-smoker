"""Creates a distribution of the POWERBAR SMOKER (POSM) package.

    Usage:
    python3 posm/setup.py bdist_egg --dist=./dist --bdist-dir=build
"""

# Standard Imports
from typing import Final
import fnmatch
import shutil
import os
# Third Party Imports
from hobo.disk_operations import delete_file, find_path_to_dir
from hobo.misc import print_exception
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as build_py_orig
# Local Imports


EXCLUDE: Final[list] = ['posm/setup.py']  # Modules to exclude from the egg


# Shamelessly lifted from: https://stackoverflow.com/a/56044136
class build_py(build_py_orig):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        return [
            (pkg, mod, file)
            for (pkg, mod, file) in modules
            if not any(fnmatch.fnmatchcase(file, pat=pattern) for pattern in EXCLUDE)
        ]


def main() -> None:
    """Facilitate calling setuptools.setup() for POSM.

    Copies posm/__main__.py to the repo's top level directory to serve as the eggsecutable's
    __main__.py.  Deletes that file upon success.  Also utilizes a "hijacked"
    setuptools.command.build_py to exclude an undesired modules that may exist in the posm
    directory.
    """
    # LOCAL VARIABLES
    project_dir_name = 'powerbar-smoker'  # Top-level directory name
    pkg_name = 'posm'                     # Package name
    pkg_version = '1.0'                   # Package version
    found_pkgs = find_packages()          # Should result in [pkg_name]
    temp_main = ''                        # Delete this after

    # VALIDATION
    if project_dir_name not in os.getcwd():
        raise RuntimeError(f'The current working directory must contain {project_dir_name}')
    if not found_pkgs:
        raise RuntimeError('No packages found. Consider changing directory to one level above '
                           'the package directory.')

    # TEMP __main__.py
    temp_main = shutil.copy('posm/__main__.py', find_path_to_dir(project_dir_name))

    # SETUP
    setup(name=pkg_name,
          version=pkg_version,
          packages=found_pkgs,
          # packages=[pkg_name],
          cmdclass={'build_py': build_py},
          author='Insider Threat',
          author_email='insider_threat@pizzabox.pizza',
          url='https://pizzabox.pizza/',
          # Module to call on $ python my.egg
          py_modules=['__main__'],
          )

    # CLEANUP
    delete_file(temp_main)


if __name__ == '__main__':
    try:
        main()
    # pylint: disable=broad-except
    except Exception as err:
        # Str wrapper is important in case err.args[0] contains an errno value
        print_exception(err)
    # pylint: enable=broad-except
