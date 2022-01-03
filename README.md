# POWERBAR SMOKER (POSM)

A Python eggsecutable that uses nmap to scan an IP address read from a file

## Purpose

Easily and quickly execute a very basic scan using an "eggsecutable" through Python.

## Usage

### Package

`python3 -m posm <file_with_an_ip_addr>`

### Eggsecutable

```
python3 light_the_powerbar.py bdist_egg --dist-dir=./dist --bdist-dir=build
python3 dist/posm-1.0-py?.?.egg <file_with_an_ip_addr>
```

### File Format

POSM will ignore any commented lines (e.g., `# This is a comment`) in the config file.  Leading and trailing whitespace will also be ignored.  Example:

```
# This config file will tell POSM to scan 3.19.27.147
3.19.27.147
```