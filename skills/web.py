from .system import search_web, open_site

def handle_web(intent: str, sites: dict):
    if intent.startswith("open ") and len(intent.split())==2:
        name = intent.split()[1]
        return open_site(name, sites)
    if intent.startswith("search for "):
        q = intent.replace("search for ", "", 1).strip()
        return search_web(q)
    return ""
