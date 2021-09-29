import random
import string


def create_random_string(size):
    return ''.join(
        random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=size)
    )