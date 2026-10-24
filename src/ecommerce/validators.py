from django.core.exceptions import ValidationError

BLOCKED_WORD = [
    "barato",
    "malo"
]

def validate_blocked_words(value):
    init_string = f"{value}".lower()
    unique_words = set(init_string.split())
    blocked_words = set(BLOCKED_WORD)
    invalid_words = (unique_words & blocked_words)
    has_error = len(invalid_words) > 0
    if has_error:
        errors = []
        for invalid_words in invalid_words:
            msg = "{} es una palabra no permitida".format(invalid_words)
            errors.append(msg)
        raise ValidationError(errors)
    return value
