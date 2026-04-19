import json
from clients import get_groq_client
from config import AUDITOR_PROMPT, MAIN_MODEL_ID


# Model Call 

def call_model(model_id: str, system: str, user: str, max_tokens: int = 600) -> str:
    """Send a chat completion request and return the text content."""
    client = get_groq_client()
    resp = client.chat.completions.create(
        model=model_id,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user},
        ],
    )
    return resp.choices[0].message.content or ""


# JSON Parsing 

def parse_audit(raw: str) -> dict:
    """Strip optional markdown fences and parse audit JSON."""
    if "```" in raw:
        for part in raw.split("```"):
            part = part.strip().lstrip("json").strip()
            if part.startswith("{"):
                raw = part
                break
    return json.loads(raw.strip())


# Audit Pipeline 

def audit_response(query: str, tutor_text: str) -> dict:
    """Run the auditor model on a tutor response and return structured results."""
    prompt = AUDITOR_PROMPT.format(query=query, response=tutor_text)
    raw = call_model(
        MAIN_MODEL_ID,
        "You are a bias detection AI. Return ONLY valid JSON.",
        prompt,
        max_tokens=900,
    )
    return parse_audit(raw)


# Colour Helper 

def score_color(v: int) -> str:
    """Map a 0-100 score to a red / amber / green hex colour."""
    if v < 35:
        return "#e05252"
    if v < 65:
        return "#fbbf24"
    return "#3ecf82"