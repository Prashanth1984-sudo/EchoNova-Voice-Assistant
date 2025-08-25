import webbrowser

def execute(command: str) -> str:
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google."
    elif command.startswith("search"):
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}."
    else:
        return "Web command not recognized."
