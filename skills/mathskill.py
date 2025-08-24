import re
from utils import safe_eval_math

MATH_PAT = re.compile(r"^(calculate|calc|what is)\s+(.+)$")

def handle_math(intent: str):
    m = MATH_PAT.match(intent)
    if not m: return ""
    expr = m.group(2).strip().replace("x", "*")
    try:
        val = safe_eval_math(expr)
        return f"The result is {val}."
    except Exception:
        return "I couldn't compute that safely."
