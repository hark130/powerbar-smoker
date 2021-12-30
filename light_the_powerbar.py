"""Creates a distribution of the POWERBAR SMOKER (POSM) package.

    Usage:
    python3 light_the_powerbar.py bdist_egg --dist-dir=./dist --bdist-dir=build
"""

# Standard Imports
import os
# Third Party Imports
from hobo.misc import print_exception
from setuptools import setup, find_packages
# Local Imports


def main() -> None:
    """Facilitate calling setuptools.setup() for POSM."""
    # LOCAL VARIABLES
    project_dir_name = 'powerbar-smoker'  # Top-level directory name
    pkg_name = 'posm'                     # Package name
    pkg_version = '1.0'                   # Package version
    found_pkgs = find_packages()          # Should result in [pkg_name]

    # VALIDATION
    if project_dir_name not in os.getcwd():
        raise RuntimeError(f'The current working directory must contain {project_dir_name}')
    if not found_pkgs:
        raise RuntimeError('No packages found. Consider changing directory to one level above '
                           'the package directory.')

    # SETUP
    setup(name=pkg_name,
          version=pkg_version,
          packages=found_pkgs,
          # packages=[pkg_name],
          author='Insider Threat',
          author_email='insider_threat@pizzabox.pizza',
          url='https://pizzabox.pizza/',
          # Module to call on $ python my.egg
          py_modules=['__main__'],
          )


if __name__ == '__main__':
    try:
        main()
    # pylint: disable=broad-except
    except Exception as err:
        # Str wrapper is important in case err.args[0] contains an errno value
        print_exception(err)
    # pylint: enable=broad-except
