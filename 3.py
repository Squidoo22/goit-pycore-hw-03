import re


def starts_with_plus(text: str) -> bool:
    pattern = r'^\+'

    return re.match(pattern, text) is not None


def normalize_phone(phone_number: str) -> str:
    normalized_phone_number = ""

    if not starts_with_plus(phone_number):
        normalized_phone_number += '+'

    for char in phone_number:
        if char.isdigit():
            normalized_phone_number += char

    return normalized_phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
