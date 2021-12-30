"""Defines the entry level POWERBAR SMOKER (POSM) API."""

# Standard Imports
# Third Party Imports
from hobo.misc import print_exception
from hobo.subprocess_wrapper import execute_subprocess_cmd
# Local Imports
from posm.config import read_config
from posm.parser import parse_arguments


def main(args: list) -> int:
    """Executes POWERBAR SMOKER (POSM).

    1. Reads the filename provided at the CLI
    2. Extracts the IPv4 address from the file
    3. Uses nmap to scan that address

    Args:
        args: A list of arguments, as strings, from the command line

    Returns:
        0 on success
        1 on bad argument(s)
        2 on bad config file
        3 on failed execution

    Raises:
        None
    """

    # LOCAL VARIABLES
    config_file = ''          # Config file name from command line args
    ip_addr = ''              # IPv4 address extracted from that file
    std_output = ''           # stdout from the scan
    std_error = ''            # stderr from the scan
    success = 0               # 0 on success, 1 on bad input, 2 on failed execution

    # PARSE ARGUMENTS
    try:
        config_file = parse_arguments(args)
    except (TypeError, ValueError, RuntimeError) as err:
        print_exception(err)
        success = 1

    # PARSE CONFIG FILE
    if config_file:
        try:
            ip_addr = read_config(config_file)
        except Exception as err:
            print_exception(err)
            success = 2

    # SCAN
    if ip_addr:
        try:
            std_output, std_error = execute_subprocess_cmd(['nmap', '-sT', '-p 1-1024', ip_addr])
        except (TypeError, ValueError, RuntimeError) as err:
            print_exception(err)
            success = 3
        else:
            if std_output:
                print(f'\n{std_output}')
            if std_error:
                print(f'\n{std_error}')

    # DONE
    return success
