"""Parse POWERBAR SMOKER (POSM) command line arguments."""


def parse_arguments(args: list) -> str:
    """Parse the command line arguments and return a single arg.

    Args:
        args: A list of arguments, as strings, from the command line

    Returns: The first command line argument

    Raises:
        TypeError: Bad type found
        ValueError: Bad value found
        RuntimeError: Wrong number of arguments
    """
    # INPUT VALIDATION
    _validate_parameters(args)

    # GET ARGUMENT
    return args[1]


def _validate_parameters(args: list) -> None:
    """
    Purpose - Validated parameters on behalf of parse_arguments()
    Param
        args - A list of arguments from the command line
    Exceptions
        TypeError if a bad data type is detected
        ValueError if a bad value is detected
        RuntimeError on usage error
    Returns
        None
    """
    # INPUT VALIDATION
    if not isinstance(args, list):
        raise TypeError(f'Invalid "args" data type of {type(args)}')
    if not args:
        raise ValueError('The "args" parameter may not be empty')
    if len(args) < 2:
        raise RuntimeError('Invalid usage: Not enough arguments')
    if len(args) > 2:
        raise RuntimeError('Invalid usage: Too many arguments')
    if not isinstance(args[1], str):
        raise TypeError(f'Invalid argument data type of {type(args[1])}')
    if not args[1]:
        raise ValueError('The command line argument may not be empty')
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError(f'Invalid data type of {type(arg)} found in '
                            '"args"')
        if not arg:
            raise ValueError('Empty parameter found in "args"')
