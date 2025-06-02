# max-context

## Introduction

If an LLM has, say, 128k tokens max context, can it really process text that big without losing focus? Especially if the text contains a lot of hard data (names and numbers)?

There is a general recommendation to stick to no more than half of the max context size. But is that recommendation correct and based on evidence?

To measure when the model loses focus, we generate increasingly long sequences of randomized sentences that look like "Dr. Kohob Zomoff is 29 years old." One such sentence is probably around 10 tokens.

Then at the end we ask the LLM a question about the first / middle / last sentence. We check then, via dichotomy, at what point it loses the ability to answer.

## Running

You need Ollama, Conda and Make installed.

To build:

```bash
make create-env
conda activate max_context
```

And then to run the different modes:

```bash
make model=mistral-nemo:12b location=beginning run
make model=mistral-nemo:12b location=middle run
make model=mistral-nemo:12b location=end run
```

## Out Of Scope

Token counts were not included, since every model uses a different tokenizer, making matters more complicated.

Reasoning models (DeepSeek R1, Qwen 3) were not a part of this experiment. They would benefit of using the Ollama 0.9.0 API.

Ollama silently cuts off the beginning of the context if the size of the context exceeds the maximum context capacity of the model. We are not handling that in any special way because it does not seem to matter for this experiment.

## Results

### mistral-nemo:12b (ID: 994f3b8b7801) 7.1 GB  

- Model mistral-nemo:12b lost focus between 296 and 304 sentences when the answer was in the beginning.
- Model mistral-nemo:12b lost focus between 384 and 392 sentences when the answer was in the middle.
- Model mistral-nemo:12b never lost focus, even at 131072 sentences, when the answer was in the end.

### devstral:24b (ID: c4b2fa0c33d7) 14 GB  

- Model devstral:24b lost focus between 288 and 296 sentences when the answer was in the beginning.
- Model devstral:24b lost focus between 296 and 304 sentences when the answer was in the middle.
- Model devstral:24b never lost focus, even at 131072 sentences, when the answer was in the end.
          
### gemma3:4b (ID: a2af6cc3eb7f) 3.3 GB  

- Model gemma3:4b lost focus between 296 and 304 sentences when the answer was in the beginning.
- Model gemma3:4b lost focus between 296 and 304 sentences when the answer was in the middle.
- Model gemma3:4b lost focus between 2040 and 2048 sentences when the answer was in the end.

### gemma3:1b (ID: 8648f39daa8f) 0.8 GB

- Model gemma3:1b lost focus between 296 and 304 sentences when the answer was in the beginning.
- Model gemma3:1b lost focus between 240 and 248 sentences when the answer was in the middle.  
- Model gemma3:1b lost focus between 240 and 248 sentences when the answer was in the end.

### llama3.1:8b (ID: 46e0c10c039e) 4.9 GB

- Model llama3.1:8b lost focus between 312 and 320 sentences when the answer was in the beginning.
- Model llama3.1:8b lost focus between 528 and 536 sentences when the answer was in the middle.
- Model llama3.1:8b never lost focus, even at 131072 sentences, when the answer was in the end.

### llama3.2:3b (ID: a80c4f17acd5) 2.0 GB

- Model llama3.2:3b lost focus between 312 and 320 sentences when the answer was in the beginning.
- Model llama3.2:3b lost focus between 512 and 520 sentences when the answer was in the middle.
- Model llama3.2:3b never lost focus, even at 131072 sentences, when the answer was in the end.
     
### qwen2.5:7b (ID: 845dbda0ea48) 4.7 GB 

- Model qwen2.5:7b lost focus between 288 and 296 sentences when the answer was in the beginning.
- Model qwen2.5:7b lost focus between 288 and 296 sentences when the answer was in the middle.
- Model qwen2.5:7b never lost focus, even at 131072 sentences, when the answer was in the end.
    
### qwen2.5:14b (ID: 7cdf5a0187d5) 9.0 GB

- Model qwen2.5:14b lost focus between 288 and 296 sentences when the answer was in the beginning.
- Model qwen2.5:14b lost focus between 320 and 328 sentences when the answer was in the middle.
- Model qwen2.5:14b never lost focus, even at 131072 sentences, when the answer was in the end.

### phi4:14b (ID: ac896e5b8b34) 9.1 GB

- Model phi4:14b lost focus between 312 and 320 sentences when the answer was in the beginning.
- Model phi4:14b lost focus between 312 and 320 sentences when the answer was in the middle.  
- Model phi4:14b never lost focus, even at 131072 sentences, when the answer was in the end.

### phi3:3.8b (ID: 4f2222927938) 2.2 GB

- Model phi3:3.8b lost focus between 256 and 264 sentences when the answer was in the beginning.
- Model phi3:3.8b lost focus between 256 and 264 sentences when the answer was in the middle.
- Model phi3:3.8b lost focus between 336 and 344 sentences when the answer was in the end.   
