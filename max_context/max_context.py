from __future__ import annotations

import random
from typing import Callable


def create_name() -> str:
    consonants = ["b", "d", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    capital_consonants = [c.upper() for c in consonants]
    sirname_suffixes = ["son", "ski", "off", "yev"]

    return (
        random.choice(capital_consonants)
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
    return "Dr. " + name + " is " + age + " years old."


def check_context(sentences: int, infer_response_function: Callable[[str], str], location: str) -> bool:
    important_name = create_name()
    important_age = create_age()
    important_sentence = create_sentence(important_name, important_age)
    question = important_sentence

    more_sentences_needed = sentences - 2  # The first sentence and the question in the end both count
    previously_appended_to_end: bool = False
    while more_sentences_needed >= 1:
        more_sentences_needed -= 1

        name = create_name()
        while name == important_name:
            name = create_name()
        new_sentence = create_sentence(name, create_age())

        if location == "beginning":
            question = question + " " + new_sentence
        elif location == "end":
            question = new_sentence + " " + question
        elif location == "middle":
            question = new_sentence + " " + question if previously_appended_to_end else question + " " + new_sentence
            previously_appended_to_end = not previously_appended_to_end
        else:
            raise NotImplementedError(location)

    question += f" How old is Dr. {important_name}?"
    response = infer_response_function(question)
    print(f"RESPONSE: {response}", flush=True)

    return important_age in response


def find_cutoff(infer_response_function: Callable[[str], str], location: str) -> tuple[int | None, int | None]:
    print("ASKING QUESTION WITH: 2 sentences", flush=True)
    if not check_context(2, infer_response_function, location):
        return None, None
    print("SUCCESS: True", flush=True)

    highest_good: int = 2
    lowest_bad: int | None = None

    while (lowest_bad is None or lowest_bad - highest_good > 10) and highest_good < 100000:
        next_attempt = int((highest_good + lowest_bad) / 2) if lowest_bad else highest_good * 2
        print(f"\nASKING QUESTION WITH: {next_attempt} sentences", flush=True)

        result = check_context(next_attempt, infer_response_function, location=location)
        print(f"SUCCESS: {result}", flush=True)
        if result:
            highest_good = next_attempt
        else:
            lowest_bad = next_attempt

    return highest_good, lowest_bad
