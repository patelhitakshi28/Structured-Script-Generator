from src.loader import load_text
from src.chunker import chunk_text
from src.summarizer import TextSummarizer
from src.script_writer import create_explainer_script


def main():
    file_path = "data/sample.txt"

    print("\n[1] Loading text...")
    text = load_text(file_path)
    print(f"Loaded {len(text.split())} words.")

    print("\n[2] Chunking text...")
    chunks = chunk_text(text, chunk_size=120, overlap=20)
    print(f"Created {len(chunks)} chunk(s).")

    print("\n[3] Summarizing chunks...")
    summarizer = TextSummarizer()
    chunk_summaries = summarizer.summarize_chunks(chunks)

    for i, summary in enumerate(chunk_summaries, start=1):
        print(f"\n--- Chunk Summary {i} ---")
        print(summary)

    print("\n[4] Creating final summary...")
    final_summary = summarizer.summarize_full_text(chunk_summaries)
    print("\nFinal Summary:")
    print(final_summary)

    print("\n[5] Creating explainer script...")
    script = create_explainer_script(final_summary)
    print("\nExplainer Script:\n")
    print(script)


if __name__ == "__main__":
    main()