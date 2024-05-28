import re


def is_valid_password(string):
    return re.match(r"(.){12,}[0-9]{1,}")
