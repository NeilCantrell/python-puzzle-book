def string_to_ascii(input_str: str) -> list[int]:
    return [ord(character) for character in input_str]


print(string_to_ascii("Programming puzzles!"))


# Bonus Solution
def ascii_to_string(input_ascii_codes: list[int]) -> str:
    return "".join([chr(input_ascii_code) for input_ascii_code in input_ascii_codes])


print(ascii_to_string([80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103, 32, 112, 117, 122, 122, 108, 101, 115, 33]))
