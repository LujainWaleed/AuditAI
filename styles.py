CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Playfair+Display:wght@700;900&family=Source+Sans+3:wght@300;400;600&display=swap');

:root {
    --bg-dark:     #0b0d12;
    --bg-card:     #111520;
    --bg-panel:    #141824;
    --accent-gold: #d4a843;
    --accent-red:  #e05252;
    --accent-green:#3ecf82;
    --accent-blue: #4a9eff;
    --text-primary:#e8eaf0;
    --text-muted:  #6b7280;
    --border:      rgba(255,255,255,0.07);
}
html, body, [class*="css"] { font-family:'Source Sans 3',sans-serif; background-color:var(--bg-dark); color:var(--text-primary); }
.stApp { background: var(--bg-dark); }
#MainMenu, footer, header { visibility: hidden; }

.ethiguard-header {
    border-bottom: 1px 
    padding: 2rem 0 1.5rem; text-align: center; margin-bottom: 2rem;
    position: relative; overflow: hidden;
}
.ethiguard-header::before {
    content:''; position:absolute; top:-60px; left:50%; transform:translateX(-50%);
    width:600px; height:200px;

}
.ethiguard-logo { font-family:'Playfair Display',serif; font-size:7px; font-weight:900; letter-spacing:-1px; color:var(--accent-gold); margin:0; }
.ethiguard-logo span { color:var(--text-primary); }
.ethiguard-tagline { font-family:'IBM Plex Mono',monospace; font-size:0.78rem; color:var(--text-muted); letter-spacing:3px; text-transform:uppercase; margin-top:0.3rem; }

.badge { display:inline-block; font-family:'IBM Plex Mono',monospace; font-size:0.62rem; padding:2px 10px; border-radius:20px; margin-top:0.5rem; }
.badge-or   { background:rgba(212,168,67,0.15); border:1px solid rgba(212,168,67,0.3); color:var(--accent-gold); }
.badge-live { background:rgba(62,207,130,0.12); border:1px solid rgba(62,207,130,0.3); color:#3ecf82; animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.6} }

.agent-label { font-family:'IBM Plex Mono',monospace; font-size:0.65rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; padding:4px 12px; border-radius:6px; display:inline-block; margin-bottom:1rem; }
.label-tutor { background:rgba(107,114,128,0.15); color:var(--text-muted);  border:1px solid rgba(107,114,128,0.2); }
.label-guard { background:rgba(212,168,67,0.12);  color:var(--accent-gold); border:1px solid rgba(212,168,67,0.25); }

.response-box { background:var(--bg-panel); border:1px solid var(--border); border-radius:8px; padding:1.2rem; font-size:0.92rem; line-height:1.8; min-height:160px; color:#c9cdd8; white-space:pre-wrap; }
.response-box.biased  { border-left:3px solid var(--accent-red); }
.response-box.audited { border-left:3px solid var(--accent-gold); }
.response-box.clean   { border-left:3px solid var(--accent-green); }

.flag-card { background:rgba(224,82,82,0.07); border:1px solid rgba(224,82,82,0.22); border-left:4px solid var(--accent-red); border-radius:8px; padding:0.9rem 1.1rem; margin-bottom:0.75rem; }
.flag-type { font-family:'IBM Plex Mono',monospace; font-size:0.65rem; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:var(--accent-red); margin-bottom:0.3rem; }
.flag-text { font-size:0.88rem; color:#d1d5db; line-height:1.5; }

.socratic-box { background:linear-gradient(135deg,rgba(74,158,255,0.08),rgba(74,158,255,0.03)); border:1px solid rgba(74,158,255,0.2); border-radius:10px; padding:1rem 1.2rem; margin-top:1rem; }
.socratic-label { font-family:'IBM Plex Mono',monospace; font-size:0.65rem; color:var(--accent-blue); letter-spacing:2px; text-transform:uppercase; margin-bottom:0.4rem; }
.socratic-text { font-style:italic; color:#b8d4ff; font-size:0.9rem; line-height:1.6; }

.scorecard { background:var(--bg-panel); border:1px solid var(--border); border-radius:10px; padding:1.1rem; margin-top:1rem; }
.scorecard-title { font-family:'IBM Plex Mono',monospace; font-size:0.65rem; color:var(--text-muted); letter-spacing:2px; text-transform:uppercase; margin-bottom:0.8rem; }
.score-row { display:flex; align-items:center; justify-content:space-between; margin-bottom:0.55rem; }
.score-label { font-size:0.82rem; color:#9ca3af; min-width:130px; }
.score-bar-track { flex:1; height:5px; background:rgba(255,255,255,0.06); border-radius:99px; margin:0 10px; overflow:hidden; }
.score-bar-fill { height:100%; border-radius:99px; }
.score-val { font-family:'IBM Plex Mono',monospace; font-size:0.75rem; min-width:32px; text-align:right; }

.section-divider {
    border-top: 1px solid var(--border);
    margin: 2rem 0 1.2rem;
    padding-top: 1.2rem;
    font-family:'IBM Plex Mono',monospace; font-size:0.65rem;
    color:var(--text-muted); letter-spacing:2px; text-transform:uppercase;
}

.model-box { background:var(--bg-card); border:1px solid var(--border); border-radius:12px; padding:1.3rem 1.2rem; text-align:center; position:relative; overflow:hidden; }
.model-box-top-bar { height:3px; border-radius:3px 3px 0 0; position:absolute; top:0; left:0; right:0; }
.model-box-name { font-family:'IBM Plex Mono',monospace; font-size:0.7rem; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:1rem; }
.model-box-overall { font-family:'Playfair Display',serif; font-size:3rem; font-weight:900; line-height:1; margin-bottom:0.2rem; }
.model-box-overall-label { font-family:'IBM Plex Mono',monospace; font-size:0.6rem; color:var(--text-muted); letter-spacing:2px; text-transform:uppercase; margin-bottom:1.2rem; }
.metric-row { display:flex; align-items:center; justify-content:space-between; margin-bottom:0.5rem; }
.metric-name { font-size:0.78rem; color:#6b7280; text-align:left; flex:1; }
.metric-bar-wrap { flex:2; margin:0 8px; }
.metric-bar-bg { height:4px; background:rgba(255,255,255,0.05); border-radius:99px; overflow:hidden; }
.metric-bar-fill { height:100%; border-radius:99px; }
.metric-pct { font-family:'IBM Plex Mono',monospace; font-size:0.72rem; font-weight:600; min-width:36px; text-align:right; }

.stTextInput>div>div>input, .stSelectbox>div>div, .stTextArea textarea {
    background:var(--bg-panel)!important; border:1px solid var(--border)!important;
    color:var(--text-primary)!important; border-radius:8px!important; font-family:'Source Sans 3',sans-serif!important;
}
.stButton>button {
    background:linear-gradient(135deg,#c49a35,#d4a843)!important; color:#0b0d12!important;
    font-family:'IBM Plex Mono',monospace!important; font-weight:600!important; font-size:0.8rem!important;
    letter-spacing:1.5px!important; text-transform:uppercase!important; border:none!important;
    border-radius:8px!important; padding:0.55rem 1.6rem!important;
}
.stButton>button:hover { background:linear-gradient(135deg,#d4a843,#e0b853)!important; box-shadow:0 0 20px rgba(212,168,67,0.3)!important; }
section[data-testid="stSidebar"] { background:var(--bg-card)!important; border-right:1px solid var(--border)!important; }
</style>
"""