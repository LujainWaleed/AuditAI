# AuditAI — AI Auditing Layer for Education

AuditAI is a Streamlit app that applies the LLM-as-a-Judge technique to detect cultural and algorithmic bias in LLM-generated educational responses.. A **Tutor agent** answers a student's question, then an **Auditor agent** scans the response for bias, scores it across four metrics, and suggests a balanced rewrite plus a Socratic follow-up question.

---

## Project Structure

```
AuditAI/
├── app.py           # Entry point — wires all modules together
├── config.py        # Model IDs, system prompts, preset queries
├── clients.py       # Cached Groq / OpenAI-compatible client
├── audit.py         # Core AI logic: call_model, audit_response, parse_audit
├── styles.py        # Full CSS block (dark theme)
├── components.py    # Reusable HTML rendering helpers
├── sidebar.py       # Sidebar controls (presets, toggles)
└── requirements.txt
```

## How It Works

1. **Tutor** (Llama 3.3 70B) answers the student query naturally.
2. **Auditor** (same model, different system prompt) returns structured JSON with:
   - `flags` — specific bias types found (Western-Centricity, Gender Stereotyping, etc.)
   - `corrected_response` — a balanced rewrite
   - `socratic_prompt` — a critical-thinking question for the student
   - `scores` — Inclusivity, Neutrality, Cultural Accuracy, Source Diversity (0–100)
   - `bias_detected` — boolean
3. The UI renders a split panel, scorecard, and optional Socratic intervention.

## Setup

```bash
pip install -r requirements.txt

# Set your Groq API key
export GROQ_API_KEY=your_key_here

streamlit run app.py
```

