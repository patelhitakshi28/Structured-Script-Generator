# Mini Explainer

A beginner-friendly NLP project that converts long-form text into a short explainer-style script using Hugging Face Transformers and Python.

## Project Goal

This project simulates a small part of an AI-powered knowledge transfer pipeline:

1. Load text from a file
2. Split long text into chunks
3. Summarize each chunk
4. Combine the summaries
5. Convert the result into a simple 3-scene explainer script

## Why I Built This

I built this project to learn the foundations of document understanding and structured text generation, which are relevant to AI products that transform complex documents into simpler, presentation-ready content.

## Features

- Text file input
- Word-based chunking with overlap
- Summarization using `facebook/bart-large-cnn`
- Final condensed summary
- Rule-based explainer script generation

## Tech Stack

- Python
- uv
- Hugging Face Transformers
- PyTorch

## Project Structure

```text
mini_explainer/
├── data/
│   └── sample.txt
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── loader.py
│   ├── chunker.py
│   ├── summarizer.py
│   └── script_writer.py
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md


Setup
1. Create the virtual environment
uv venv

2. Activate the environment

3. Install dependencies
uv add transformers torch sentencepiece accelerate

Run the project
uv run python -m src.main

Example Output

The project prints:

chunk summaries
final summary
a 3-scene explainer script

Future Improvements
sentence-based chunking
PDF input support
better script generation
scene title generation
text-to-speech integration
slide or video generation

Author : Hitakshi Patel