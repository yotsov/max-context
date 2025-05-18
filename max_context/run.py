from functools import partial

from max_context.max_context import find_cutoff
from max_context.ollama_client import infer_response


def main(model: str) -> None:
    highest_good, lowest_bad = find_cutoff(partial(infer_response, model=model))
    print(f"\nFor model {model} the focus is lost somewhere between {highest_good} and {lowest_bad} sentences of context.")
