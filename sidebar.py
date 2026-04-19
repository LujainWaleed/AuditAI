import streamlit as st
from config import PRESET_QUERIES


def render_sidebar() -> dict:
    """
    Render the sidebar and return a dict with:
      - preset (str): selected preset query or empty string
      - show_socratic (bool)
      - show_scores (bool)
    """
    with st.sidebar:
        st.markdown(
            "<p style=\"font-family:'IBM Plex Mono',monospace;font-size:0.65rem;"
            "letter-spacing:2px;text-transform:uppercase;color:#6b7280;margin-bottom:1rem\">CONTROL PANEL</p>",
            unsafe_allow_html=True,
        )

        st.markdown("**Quick Scenarios**")
        preset = st.selectbox("Preset", PRESET_QUERIES, label_visibility="collapsed")

        st.markdown("<hr style='border-color:rgba(255,255,255,0.07);margin:1rem 0'>", unsafe_allow_html=True)
        show_socratic = st.toggle("Socratic Intervention", value=True)
        show_scores   = st.toggle("Bias Scorecard", value=True)

        st.markdown("<hr style='border-color:rgba(255,255,255,0.07);margin:1rem 0'>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:#4b5563;line-height:1.9">
            <p style="color:#6b7280;letter-spacing:2px;text-transform:uppercase;font-size:0.6rem">ARCHITECTURE</p>
            Tutor &nbsp; → <span style="color:#fd79a8">Llama 3.3 70B</span><br>
            Auditor → <span style="color:#fd79a8">Llama 3.3 70B</span><br>
            Provider → <span style="color:#3ecf82">Groq (free)</span>
        </div>""", unsafe_allow_html=True)

    selected_preset = "" if preset == "— type your own below —" else preset
    return {
        "preset": selected_preset,
        "show_socratic": show_socratic,
        "show_scores": show_scores,
    }