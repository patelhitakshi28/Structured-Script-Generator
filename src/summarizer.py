from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class TextSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Load tokenizer and seq2seq model directly.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def summarize_chunk(
        self,
        text: str,
        max_length: int = 80,
        min_length: int = 30
    ) -> str:
        """
        Summarize a single chunk of text using model.generate().
        """
        if len(text.split()) < 20:
            return text

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        summary_ids = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            early_stopping=True
        )

        summary = self.tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        return summary

    def summarize_chunks(self, chunks: list[str]) -> list[str]:
        """
        Summarize multiple chunks one by one.
        """
        return [self.summarize_chunk(chunk) for chunk in chunks]

    def summarize_full_text(self, chunk_summaries: list[str]) -> str:
        """
        Combine chunk summaries and summarize again.
        """
        combined = " ".join(chunk_summaries)
        return self.summarize_chunk(combined, max_length=120, min_length=50)