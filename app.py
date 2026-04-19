import streamlit as st

from styles     import CUSTOM_CSS
from sidebar    import render_sidebar
from audit      import audit_response, call_model
from config     import MAIN_MODEL_ID, TUTOR_SYSTEM
from components import (
    render_header,
    render_query_banner,
    render_status_banner,
    render_tutor_panel,
    render_auditor_panel,
    render_scorecard,
    render_socratic,
    render_placeholder,
    render_footer,
)

# Page Config 
st.set_page_config(
    page_title="AuditAI",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Styles & Header 
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
render_header()

# Sidebar 
settings = render_sidebar()

# Query Input 
query = st.text_input(
    "Student Query",
    value=settings["preset"],
    placeholder="Ask any educational question… e.g. 'Who invented algebra?'",
    label_visibility="collapsed",
)
run = st.button("▶")

if run and not query.strip():
    st.warning("Please enter a question first.")
    st.stop()

# Main Pipeline 
if run and query.strip():
    render_query_banner(query)

    # Step 1: Tutor response
    with st.spinner("Llama 3.3 generating educational response…"):
        tutor_response = call_model(MAIN_MODEL_ID, TUTOR_SYSTEM, query)

    # Step 2: Audit the tutor response
    with st.spinner("Llama 3.3 Auditor scanning for biases…"):
        try:
            audit = audit_response(query, tutor_response)
        except Exception as e:
            st.error(f"Auditor error: {e}")
            st.stop()

    flags      = audit.get("flags", [])
    corrected  = audit.get("corrected_response", "")
    socratic   = audit.get("socratic_prompt", "")
    scores     = audit.get("scores", {})
    bias_found = audit.get("bias_detected", False)

    # Status banner
    render_status_banner(bias_found, flags, scores)

    # Split panel: tutor (left) | auditor (right)
    left, right = st.columns(2, gap="medium")
    with left:
        render_tutor_panel(tutor_response, bias_found)
    with right:
        render_auditor_panel(flags, corrected)

    # Scorecard + Socratic prompt
    if settings["show_scores"] and scores:
        st.markdown("<div style='margin-top:1.5rem'></div>", unsafe_allow_html=True)
        sc_col, sq_col = st.columns(2, gap="medium")

        with sc_col:
            render_scorecard(scores)

        with sq_col:
            if settings["show_socratic"] and socratic:
                render_socratic(socratic)

# Placeholder (nothing submitted yet) 
elif not run:
    render_placeholder()

# Footer 
render_footer()