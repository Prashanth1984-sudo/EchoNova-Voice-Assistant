import wikipedia

wikipedia.set_lang("en")

def wiki_summary(query: str, sentences=2) -> str:
    try:
        return wikipedia.summary(query, sentences=sentences, auto_suggest=True, redirect=True)
    except wikipedia.DisambiguationError as e:
        return f"That has multiple meanings: {', '.join(e.options[:5])}."
    except wikipedia.PageError:
        return "I couldn't find that on Wikipedia."
    except Exception:
        return "Sorry, Wikipedia is unavailable now."
