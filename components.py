import streamlit as st
from audit import score_color


# Header 

def render_header():
    st.markdown("""
    <div class="ethiguard-header">
        <p class="ethiguard-logo">Audit<span>AI</span></p>
        <p class="ethiguard-tagline">AI Auditing Layer for Education</p>
        <span class="badge badge-live">● LIVE AI</span>
    </div>
    """, unsafe_allow_html=True)


# Query Banner 

def render_query_banner(query: str):
    st.markdown(f"""
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;
         padding:0.8rem 1.4rem;margin:1rem 0;display:flex;align-items:center;gap:1rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:var(--text-muted);
              letter-spacing:2px;text-transform:uppercase;white-space:nowrap">STUDENT QUERY</span>
        <span style="color:var(--text-primary);font-size:0.95rem;font-style:italic">"{query}"</span>
    </div>
    """, unsafe_allow_html=True)


# Status Banner 

def render_status_banner(bias_found: bool, flags: list, scores: dict):
    if bias_found:
        overall = int(sum(scores.values()) / max(len(scores), 1))
        rc = "#e05252" if overall < 35 else "#fbbf24"
        st.markdown(f"""
        <div style="background:rgba(224,82,82,0.07);border:1px solid rgba(224,82,82,0.2);
             border-radius:8px;padding:0.7rem 1.2rem;margin-bottom:1rem;display:flex;align-items:center;gap:0.8rem">
            <span style="font-size:1.2rem">⚠️</span>
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.75rem;color:{rc}">
                {len(flags)} BIAS FLAG{'S' if len(flags) != 1 else ''} DETECTED &nbsp;·&nbsp; Overall Score: {overall}%
            </span>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background:rgba(62,207,130,0.07);border:1px solid rgba(62,207,130,0.2);
             border-radius:8px;padding:0.7rem 1.2rem;margin-bottom:1rem">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.75rem;color:#3ecf82">
                ✓ NO SIGNIFICANT BIAS DETECTED — Response appears balanced and inclusive.
            </span>
        </div>""", unsafe_allow_html=True)


# Split Panel 

def render_tutor_panel(tutor_response: str, bias_found: bool):
    """Left column: raw tutor response."""
    st.markdown('<span class="agent-label label-tutor">Agent 1 · Llama 3.3 Tutor</span>', unsafe_allow_html=True)
    box_class = "biased" if bias_found else "clean"
    st.markdown(f'<div class="response-box {box_class}">{tutor_response}</div>', unsafe_allow_html=True)
    st.markdown(
        "<div style=\"font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:#374151;margin-top:0.5rem\">"
        "MODEL: openai/gpt-4o · ROLE: Standard educational response</div>",
        unsafe_allow_html=True,
    )


def render_auditor_panel(flags: list, corrected: str):
    """Right column: bias flags and corrected response."""
    st.markdown('<span class="agent-label label-guard">Agent 2 · Llama 3.3 Auditor</span>', unsafe_allow_html=True)

    if flags:
        for flag in flags:
            st.markdown(f"""
            <div class="flag-card">
                <div class="flag-type">🚩 {flag.get('type', 'BIAS')}</div>
                <div class="flag-text">{flag.get('description', '')}</div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background:rgba(62,207,130,0.07);border:1px solid rgba(62,207,130,0.2);
             border-radius:8px;padding:0.9rem 1.1rem;margin-bottom:0.75rem">
            <div style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#3ecf82;margin-bottom:0.3rem">✓ NO FLAGS</div>
            <div style="font-size:0.88rem;color:#d1d5db">The AI response appears culturally balanced and inclusive.</div>
        </div>""", unsafe_allow_html=True)

    if corrected:
        st.markdown(f"""
        <div style="margin-top:0.8rem">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#3ecf82;letter-spacing:2px;text-transform:uppercase">✓ BALANCED RESPONSE</span>
            <div class="response-box audited" style="margin-top:0.5rem;font-size:0.88rem">{corrected}</div>
        </div>""", unsafe_allow_html=True)


# Scorecard 

def render_scorecard(scores: dict):
    st.markdown(
        '<div class="scorecard"><div class="scorecard-title">📊 BIAS SCORECARD — Llama 3.3 Response</div>',
        unsafe_allow_html=True,
    )
    for metric, value in scores.items():
        c = score_color(value)
        st.markdown(f"""
        <div class="score-row">
            <span class="score-label">{metric}</span>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:{value}%;background:{c}"></div></div>
            <span class="score-val" style="color:{c}">{value}%</span>
        </div>""", unsafe_allow_html=True)

    overall = int(sum(scores.values()) / len(scores))
    oc = score_color(overall)
    st.markdown(f"""
        <div style="border-top:1px solid var(--border);margin-top:0.6rem;padding-top:0.6rem;
              display:flex;justify-content:space-between;align-items:center">
            <span style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;color:#9ca3af">OVERALL</span>
            <span style="font-family:'IBM Plex Mono',monospace;font-size:1.1rem;font-weight:600;color:{oc}">{overall}%</span>
        </div></div>""", unsafe_allow_html=True)


# Socratic Prompt 

def render_socratic(socratic: str):
    st.markdown(f"""
    <div class="scorecard" style="height:100%">
        <div class="scorecard-title">SOCRATIC INTERVENTION</div>
        <div class="socratic-box">
            <div class="socratic-label">CRITICAL THINKING PROMPT</div>
            <div class="socratic-text">"{socratic}"</div>
        </div>
        <p style="font-size:0.82rem;color:#6b7280;margin-top:1rem;line-height:1.6">
            Builds <strong style="color:#d4a843">Algorithmic Literacy</strong> —
            the ability to critically evaluate AI-generated content for embedded bias.
        </p>
    </div>""", unsafe_allow_html=True)


# Placeholder 
def render_placeholder():
    st.markdown("""
    <div style="background:var(--bg-card);border:1px dashed rgba(255,255,255,0.07);
         border-radius:12px;padding:3rem;text-align:center;margin-top:1rem">
        <div style="font-size:3rem;margin-bottom:1rem">🛡️</div>
        <p style="font-family:'Playfair Display',serif;font-size:1.4rem;color:#6b7280;margin:0">
            Enter a question and click <strong style="color:#d4a843">▶</strong>
        </p>
        <p style="font-size:0.85rem;color:#374151;margin-top:0.6rem;max-width:520px;
             margin-left:auto;margin-right:auto;line-height:1.8">
            <strong style="color:#74b9ff">Llama 3.3</strong> answers & gets audited above.<br>
        </p>
    </div>""", unsafe_allow_html=True)



# Footer 

def render_footer():
    st.markdown("<div style='margin-top:3rem'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border-top:1px solid rgba(255,255,255,0.05);padding-top:1rem;text-align:center">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:#374151">
             Lujain Aljahdali 
        </span>
    </div>""", unsafe_allow_html=True)