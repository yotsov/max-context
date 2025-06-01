from functools import partial

from max_context.max_context import find_cutoff
from max_context.ollama_client import infer_response


def main(model: str, location: str) -> None:
    if location not in {"beginning", "end", "middle"}:
        raise NotImplementedError(location)
    highest_good, lowest_bad = find_cutoff(partial(infer_response, model=model), location=location)
    if highest_good is None:
        print(f"\nModel {model} did not answer successfully even the shortest question, something went wrong.", flush=True)
    elif lowest_bad is None:
        print(f"\nModel {model} never lost focus, even at {highest_good} sentences, when the answer was in the {location}.", flush=True)
    else:
        print(f"\nModel {model} lost focus between {highest_good} and {lowest_bad} sentences when the answer was in the {location}.", flush=True)
