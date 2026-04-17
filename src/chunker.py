def chunk_text(text: str, chunk_size: int = 120, overlap: int = 20) -> list[str]:
    words = text.split()

    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap.")

    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = words[start:end]
        chunks.append(" ".join(chunk))

        if end >= len(words):
            break

        start = end - overlap

    return chunks