# max-context

Measure the maximum context size for different LLM models before they lose focus.

You need ollama and conda installed.

```bash
make create-env
conda activate max_context
make model=mistral:7b-instruct-v0.3-q4_K_M run
```

The above should give something along the lines of:

For model mistral:7b-instruct-v0.3-q4_K_M the focus is lost somewhere between 280 and 288 sentences of context.
