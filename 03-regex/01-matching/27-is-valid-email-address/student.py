import re


def is_valid_email_address(string):
    return re.fullmatch(r"[a-z0-9.]+@{1}(student\.)?ucll\.be", string)
