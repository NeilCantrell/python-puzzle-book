def has_vowel(string: str) -> bool:
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            return True
    return False


def filter_vowels(strings: list[str]) -> list[str]:
    return [s for s in strings if has_vowel(s)]


print(filter_vowels(["apple", "banana", "zyxvb"]))
