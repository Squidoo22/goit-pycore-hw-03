import random
from typing import List


def get_numbers_ticket(min: int = 1, max: int = 1000, quantity: int = 5) -> list[int]:
    if not (1 <= min <= 1000):
        raise ValueError(f"'min' must be between 1 and 1000. Got {min}.")
    if not (1 <= max <= 1000):
        raise ValueError(f"'max' must be between 1 and 1000. Got {max}.")
    if min > max:
        raise ValueError(f"'min' cannot be greater than 'max'. Got min={min}, max={max}.")

    unique_set = set()
    while len(unique_set) < quantity:
        unique_set.add(random.randint(min, max))

    return sorted(unique_set)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
