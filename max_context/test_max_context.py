from max_context.max_context import check_context, create_age, create_name, create_sentence, find_cutoff


def test_create_name() -> None:
    assert create_name() != create_name()
    assert (len(create_name())) == 16


def test_create_age() -> None:
    assert create_age() != create_age()
    assert int(create_age()) >= 25
    assert int(create_age()) <= 95


example_sentence = "Mr. Kohob Zomoff is 29 years old. "


def test_create_sentence() -> None:
    assert len(create_sentence(create_name(), create_age())) == len(example_sentence)


cutoff = 25  # At and above this value the dummy LLM loses focus


def infer_response_dummy(question: str) -> str:
    sentences = question.count(".") / 2 + 1  # Divide by 2 to account for honorific, and add 1 for the question in the end
    if sentences >= cutoff:
        return "I don't know."
    return question[: len(example_sentence)]


def infer_response_bad_dummy(_: str) -> str:
    return "I don't know."


def test_check_context() -> None:
    assert check_context(cutoff - 2, infer_response_dummy)
    assert check_context(cutoff - 1, infer_response_dummy)
    assert not check_context(cutoff, infer_response_dummy)
    assert not check_context(cutoff + 1, infer_response_dummy)

    assert not check_context(cutoff - 2, infer_response_bad_dummy)
    assert not check_context(cutoff - 1, infer_response_bad_dummy)
    assert not check_context(cutoff, infer_response_bad_dummy)
    assert not check_context(cutoff + 1, infer_response_bad_dummy)


def test_find_cutoff() -> None:
    highest_good, lowest_bad = find_cutoff(infer_response_dummy)
    assert highest_good == 24
    assert lowest_bad == 32

    highest_good, lowest_bad = find_cutoff(infer_response_bad_dummy)
    assert highest_good == 0
    assert lowest_bad == 0
