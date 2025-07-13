import wikipedia

def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=5)
        return summary
    except wikipedia.exceptions.PageError:
        return "No article found for this query."
    except wikipedia.exceptions.DisambiguationError:
        return "Query is ambiguous, please be more specific."
