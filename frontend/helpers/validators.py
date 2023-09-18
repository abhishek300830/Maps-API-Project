import re

def validate_string(string):
    pattern = "[a-zA-Z1-9- ]+"
    matcher = re.fullmatch(pattern,string)
    return matcher



