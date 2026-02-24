import re


def validate_email(email: str) -> bool:
    return re.match(
        r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
        r"@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$",
        email,
    )


def validate_password(password_string: str) -> bool:
    return re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])", password_string)
