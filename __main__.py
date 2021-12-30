"""Permits the POWERBAR SMOKER (POSM) egg distribution to be 'eggsecutable'.

    Usage: python posm.egg <file_with_an_ip_addr>  # This should be enough
"""

# Standard Imports
import sys
# Third Party Imports
# Local Imports
from posm.main import main


def eggsecute(args: list) -> int:
    """
    Purpose - Execute the POWERBAR SMOKER (POSM) API
    Param
        args - A list of arguments, as strings, from the command line
    Returns
        An error code from POSM execution
    """
    return main(args)


if __name__ == '__main__':
    # NOTE: From pydocs...
    # Most systems require [sys.exit([arg])'s optional argument arg] to
    #   be in the range 0–127, and produce undefined results otherwise.
    sys.exit(eggsecute(sys.argv))
