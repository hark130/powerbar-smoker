"""Parse the config file contents on behalf of POWERBAR SMOKER (POSM)."""

# Standard Imports
from ipaddress import AddressValueError
# Third Party Imports
from hobo.disk_operations import validate_file
from hobo.network import is_valid_ipv4_addr
# Local Imports


def read_config(filename: str) -> str:
    """Retrieves and validates the IP address from filename.

    Reads filename, removes whitespace, validates what it finds as an IPv4 address and returns it.

    Args:
        filename: Relative or absolute filename from which to extract an IPv4 address.

    Returns: The IPv4 address read from filename, as a string, on success.

    Raises:
        FileNotFoundError: filename is not found.
        OSError: filename is not a file.
        TypeError: Invalid data type.
        ValueError: filename is empty.
        AddressValueError: The contents of filename do not constitute a valid IPv4 address.
    """
    # LOCAL VARIABLES
    file_contents = ''  # Contents of the config file

    # INPUT VALIDATION
    validate_file(filename=filename, param_name='filename', must_exist=True)

    # READ CONFIG CONTENTS
    file_contents = _load_config(filename)

    # VERIFY CONTENTS
    if not is_valid_ipv4_addr(file_contents):
        raise AddressValueError(f'{file_contents} is not a valid IPv4 address')

    # DONE
    return file_contents


def _load_config(filename: str) -> str:
    """Retrieves the filenames contents, free of whitespace.

    Args:
        filename: Relative or absolute filename from which to extract an IPv4 address.

    Returns: The contents of filename, as a string, on success.
    """
    # LOCAL VARIABLES
    file_contents = ''

    # READ
    with open(filename, 'r') as in_file:
        file_contents = in_file.read()

    # DONE
    return file_contents.strip()
