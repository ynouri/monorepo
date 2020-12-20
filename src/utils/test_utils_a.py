from utils.utils_a import sum_two_numbers
from time import sleep


MAX_NB_OF_CHARS_PER_LINE = [
    "PEP-8 uses 79 characters --------- while Black uses 88"
]


def test_sum_two_numbers():
    assert sum_two_numbers(1, 5) == 6
    sleep(10)
