def create_explainer_script(summary: str) -> str:
    sentences = [s.strip() for s in summary.split(".") if s.strip()]

    if len(sentences) < 3:
        while len(sentences) < 3:
            sentences.append("Additional supporting explanation")

    script = f"""
Scene 1: Introduction
Voiceover: {sentences[0]}.

Scene 2: Main Idea
Voiceover: {sentences[1]}.

Scene 3: Conclusion
Voiceover: {sentences[2]}.
""".strip()

    return script