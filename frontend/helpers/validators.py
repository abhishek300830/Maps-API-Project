import re

def validate_string(string):
    pattern = "^[a-zA-Z][a-zA-Z1-9- ]{3,}"
    matcher = re.fullmatch(pattern,string)
    return matcher



