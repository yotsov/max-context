import random
from typing import Callable


def create_name() -> str:
    consonants = ["b", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    capital_consonants = [c.upper() for c in consonants]
    honorifics = ["Mr.", "Ms."]
    sirname_suffixes = ["son", "ski", "off", "yev"]

    return (
        random.choice(honorifics)
        + " "
        + random.choice(capital_consonants)
        + random.choice(vowels)
        + random.choice(consonants)
        + random.choice(vowels)
        + random.choice(consonants)
        + " "
        + random.choice(capital_consonants)
        + random.choice(vowels)
        + random.choice(consonants)
        + random.choice(sirname_suffixes)
    )


def create_age() -> str:
    return str(random.randint(25, 95))


def create_sentence(name: str, age: str) -> str:
    return name + " is " + age + " years old. "


def check_context(sentences: int, infer_response_function: Callable[[str], str]) -> bool:
    first_name = create_name()
    first_age = create_age()
    first_sentence = create_sentence(first_name, first_age)
    question = first_sentence

    more_sentences_needed = sentences - 2  # The first sentence and the question in the end both count
    while more_sentences_needed >= 1:
        more_sentences_needed -= 1

        name = create_name()
        while name == first_name:
            name = create_name()
        question += create_sentence(name, create_age())

    question += f"How old is {first_name}?"
    print("QUESTION:")
    print(question)

    response = infer_response_function(question)
    print("RESPONSE:")
    print(response)

    return first_age in response


def find_cutoff(infer_response_function: Callable[[str], str]) -> tuple[int, int]:
    print("\nNEXT ATTEMPT: 2 sentences")
    if not check_context(2, infer_response_function):
        return 0, 0

    highest_good: int = 2
    lowest_bad: int | None = None

    while lowest_bad is None or lowest_bad - highest_good > 10:
        next_attempt = int((highest_good + lowest_bad) / 2) if lowest_bad else highest_good * 2
        print(f"\nNEXT ATTEMPT: {next_attempt} sentences")

        result = check_context(next_attempt, infer_response_function)
        print(f"SUCCESS: {result}")
        if result:
            highest_good = next_attempt
        else:
            lowest_bad = next_attempt

    return highest_good, lowest_bad
