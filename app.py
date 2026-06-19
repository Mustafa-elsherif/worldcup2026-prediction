import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="World Cup 2026 Predictions",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif !important;
    background-color: #F8F9FB !important;
    color: #111111 !important;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2rem !important;
    max-width: 1200px !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #1a6b3c 0%, #2d9e5f 100%);
    border-radius: 18px;
    padding: 40px 36px;
    color: white;
    margin-bottom: 24px;
}
.hero .badge {
    background: rgba(255,255,255,0.2);
    border-radius: 30px;
    padding: 4px 14px;
    font-size: 0.76rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
    color: white;
}
.hero h1 { font-size: 2rem; font-weight: 700; margin: 0 0 8px; color: white; }
.hero p  { font-size: 0.95rem; opacity: 0.9; margin: 0; color: white; }

/* Metric cards */
.metric-row { display: flex; gap: 14px; margin-bottom: 24px; }
.metric-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    flex: 1;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    border: 1px solid #E4EAF0;
}
.metric-card .val { font-size: 1.8rem; font-weight: 700; color: #1a6b3c; }
.metric-card .lbl { font-size: 0.72rem; color: #666; font-weight: 600;
                    text-transform: uppercase; letter-spacing: 0.7px; margin-top: 4px; }

/* Section title */
.sec { font-size: 1rem; font-weight: 700; color: #111;
       margin: 0 0 12px; padding-bottom: 8px; border-bottom: 2px solid #D4EDE0; }

/* Rank table row */
.rank-row {
    display: flex; align-items: center; justify-content: space-between;
    background: white; border-radius: 10px; padding: 10px 14px;
    margin-bottom: 7px; border: 1px solid #EAEEF2;
}
.rank-row:hover { border-color: #2d9e5f; }
.rank-num  { font-size: 0.8rem; color: #aaa; font-weight: 600; width: 28px; }
.rank-name { font-size: 0.95rem; font-weight: 600; color: #111; flex: 1; }
.rank-goals{ font-size: 0.88rem; color: #444; margin-right: 12px; }
.rank-badge{
    font-size: 0.72rem; font-weight: 700; padding: 3px 10px;
    border-radius: 20px; color: white;
}

/* Expander */
div[data-testid="stExpander"] {
    background: white !important;
    border: 1px solid #E4EAF0 !important;
    border-radius: 10px !important;
    margin-bottom: 6px !important;
}
div[data-testid="stExpander"] summary {
    font-weight: 600 !important;
    color: #111 !important;
    font-size: 0.95rem !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] { color: #555 !important; font-weight: 500 !important; }
.stTabs [aria-selected="true"] { color: #1a6b3c !important; font-weight: 700 !important; }

/* Info box */
.ibox {
    background: #F0FAF4; border-left: 4px solid #1a6b3c;
    border-radius: 8px; padding: 14px 16px;
    font-size: 0.87rem; color: #1a3a28;
    margin-bottom: 12px; line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.DataFrame({
        "country": [
            "France","Argentina","Netherlands","Brazil","England","Germany",
            "Croatia","Spain","Sweden","Uruguay","Switzerland","Belgium",
            "Paraguay","Portugal","Colombia","United States","Curacao",
            "Uzbekistan","DR Congo","Jordan","Turkiye","Czechia",
            "Cabo Verde","Cote d'Ivoire","Morocco","South Korea","Norway",
            "Scotland","Austria","Bosnia & Herz.","Ecuador","Qatar",
            "Mexico","Australia","South Africa","Senegal","Algeria",
            "Japan","Tunisia","Ghana","Saudi Arabia","Iran","Canada",
            "Egypt","New Zealand","Panama","Iraq","Haiti"
        ],
        "total_goals": [
            11.82,10.26,9.90,9.27,8.96,8.61,
            6.29,7.58,6.48,6.10,5.77,6.37,
            5.05,6.68,5.59,2.75,5.08,
            5.08,5.08,5.08,5.08,5.08,
            5.08,5.08,4.22,4.04,4.75,
            4.86,6.12,4.51,5.16,3.32,
            2.94,3.55,3.55,3.91,4.13,
            3.58,3.24,4.03,3.50,3.32,2.01,
            2.68,2.27,1.97,1.95,1.65
        ],
        "stage": [
            "champion","runnerup","sf","sf","qf","qf",
            "qf","qf","roundof16","roundof16","roundof16","roundof16",
            "roundof16","roundof16","roundof16","roundof16","roundof32",
            "roundof32","roundof32","roundof32","roundof32","roundof32",
            "roundof32","roundof32","roundof32","roundof32","roundof32",
            "roundof32","roundof32","roundof32","roundof32","roundof32",
            "group","group","group","group","group",
            "group","group","group","group","group","group",
            "group","group","group","group","group"
        ],
    })
    df["rank"] = range(1, len(df)+1)
    return df

df = load_data()

STAGE_COLOR = {
    "champion":  "#D4A017",
    "runnerup":  "#6B7280",
    "sf":        "#1D4ED8",
    "qf":        "#6D28D9",
    "roundof16": "#B45309",
    "roundof32": "#C2410C",
    "group":     "#374151",
}
STAGE_LABEL = {
    "champion":  "🏆 Champion",
    "runnerup":  "🥈 Runner-up",
    "sf":        "Semi-finals",
    "qf":        "Quarter-finals",
    "roundof16": "Round of 16",
    "roundof32": "Round of 32",
    "group":     "Group Stage",
}

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">⚽ FIFA World Cup 2026 · Zindi ML Challenge</div>
  <h1>World Cup 2026 Predictions</h1>
  <p>Machine learning predictions for 48 nations — goals scored & tournament stage reached</p>
</div>
""", unsafe_allow_html=True)

# ── Metrics ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="metric-row">
  <div class="metric-card"><div class="val">48</div><div class="lbl">Teams Predicted</div></div>
  <div class="metric-card"><div class="val">3.95</div><div class="lbl">Best RMSE</div></div>
  <div class="metric-card"><div class="val">0.41</div><div class="lbl">Best F1 Score</div></div>
  <div class="metric-card"><div class="val">17</div><div class="lbl">Features Used</div></div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🌍  Predictions", "📊  Model Performance", "🔍  Feature Importance"])

# ════════════════════════════════════════════════════
# TAB 1 — Predictions
# ════════════════════════════════════════════════════
with tab1:
    left, right = st.columns([1, 1.6], gap="large")

    with left:
        st.markdown('<div class="sec">🏆 Tournament Bracket</div>', unsafe_allow_html=True)
        stages_order = [
            ("champion",  "🏆 Champion"),
            ("runnerup",  "🥈 Runner-up"),
            ("sf",        "🔵 Semi-finals"),
            ("qf",        "🟣 Quarter-finals"),
            ("roundof16", "🟡 Round of 16"),
            ("roundof32", "🟠 Round of 32"),
            ("group",     "⚫ Group Stage"),
        ]
        for key, label in stages_order:
            teams = df[df["stage"] == key]
            expanded = key in ["champion","runnerup","sf","qf"]
            with st.expander(f"{label}  ({len(teams)})", expanded=expanded):
                for _, row in teams.iterrows():
                    color = STAGE_COLOR[key]
                    st.markdown(
                        f"<div style='padding:5px 0; color:#111; font-size:14px;'>"
                        f"<span style='background:{color};color:white;border-radius:4px;"
                        f"padding:2px 7px;font-size:11px;font-weight:700;margin-right:8px;'>"
                        f"{STAGE_LABEL[key]}</span>"
                        f"<strong>{row['country']}</strong> &nbsp;·&nbsp; "
                        f"<span style='color:#444'>{row['total_goals']:.1f} goals</span></div>",
                        unsafe_allow_html=True
                    )

    with right:
        st.markdown('<div class="sec">🥅 Predicted Goals — Top 20</div>', unsafe_allow_html=True)
        top20 = df.sort_values("total_goals", ascending=False).head(20).copy()
        top20["stage_label"] = top20["stage"].map(STAGE_LABEL)

        fig1 = px.bar(
            top20, x="total_goals", y="country", orientation="h",
            color="stage",
            color_discrete_map=STAGE_COLOR,
            labels={"total_goals": "Predicted Goals", "country": "", "stage": "Stage"},
            text="total_goals",
        )
        fig1.update_traces(texttemplate="%{text:.1f}", textposition="outside",
                           textfont=dict(size=11, color="#111"))
        fig1.update_layout(
            height=540,
            plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13, color="#111"),
            yaxis=dict(categoryorder="total ascending", tickfont=dict(size=13, color="#111")),
            xaxis=dict(showgrid=True, gridcolor="#F0F0F0", tickfont=dict(color="#555")),
            legend=dict(orientation="h", yanchor="bottom", y=1.02,
                        font=dict(size=11, color="#111")),
            margin=dict(l=10, r=60, t=40, b=10),
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Rankings table instead of scatter
        st.markdown('<div class="sec">📋 Full Rankings — All 48 Teams</div>', unsafe_allow_html=True)
        rank_df = df.copy()
        rank_df["Stage"] = rank_df["stage"].map(STAGE_LABEL)
        rank_df["Goals"] = rank_df["total_goals"].apply(lambda x: f"{x:.1f}")
        rank_df = rank_df[["rank","country","Goals","Stage"]].rename(
            columns={"rank":"#","country":"Country"}
        )
        st.dataframe(rank_df, use_container_width=True, hide_index=True, height=280)

# ════════════════════════════════════════════════════
# TAB 2 — Model Performance
# ════════════════════════════════════════════════════
with tab2:
    model_results = {
        "Random Forest": {"RMSE": 3.9516, "F1": 0.4107},
        "XGBoost":       {"RMSE": 4.2134, "F1": 0.3717},
        "LightGBM":      {"RMSE": 4.3412, "F1": 0.3602},
    }
    models    = list(model_results.keys())
    rmse_vals = [model_results[m]["RMSE"] for m in models]
    f1_vals   = [model_results[m]["F1"]   for m in models]
    clr       = ["#1a6b3c" if m == "Random Forest" else "#A8D5BC" for m in models]
    txt_clr   = ["white"   if m == "Random Forest" else "#111"    for m in models]

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div class="sec">📉 RMSE — Goals Prediction</div>', unsafe_allow_html=True)
        st.caption("Lower is better ↓")
        fig2 = go.Figure(go.Bar(
            x=models, y=rmse_vals, marker_color=clr,
            text=[f"{v:.4f}" for v in rmse_vals],
            textposition="outside",
            textfont=dict(size=13, color="#111"),
        ))
        fig2.update_layout(
            height=300, plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13, color="#111"),
            yaxis=dict(range=[3.5, 4.6], showgrid=True, gridcolor="#EEE",
                       tickfont=dict(color="#555")),
            xaxis=dict(tickfont=dict(color="#111", size=13)),
            margin=dict(l=0,r=0,t=10,b=10), showlegend=False,
        )
        st.plotly_chart(fig2, use_container_width=True)

    with c2:
        st.markdown('<div class="sec">📈 F1 Score — Stage Prediction</div>', unsafe_allow_html=True)
        st.caption("Higher is better ↑")
        fig3 = go.Figure(go.Bar(
            x=models, y=f1_vals, marker_color=clr,
            text=[f"{v:.4f}" for v in f1_vals],
            textposition="outside",
            textfont=dict(size=13, color="#111"),
        ))
        fig3.update_layout(
            height=300, plot_bgcolor="white", paper_bgcolor="white",
            font=dict(family="Inter", size=13, color="#111"),
            yaxis=dict(range=[0.30, 0.46], showgrid=True, gridcolor="#EEE",
                       tickfont=dict(color="#555")),
            xaxis=dict(tickfont=dict(color="#111", size=13)),
            margin=dict(l=0,r=0,t=10,b=10), showlegend=False,
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown('<div class="sec">📋 Full Comparison</div>', unsafe_allow_html=True)
    res_df = pd.DataFrame([
        {"Model": m,
         "RMSE ↓ (lower = better)": f"{v['RMSE']:.4f}",
         "F1 Score ↑ (higher = better)": f"{v['F1']:.4f}",
         "Result": "✅ Selected" if m == "Random Forest" else "—"}
        for m, v in model_results.items()
    ])
    st.dataframe(res_df, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="ibox">
    <strong>📌 Final Score Formula:</strong><br>
    Overall Score = 0.60 × RMSE(Goals) + 0.40 × F1(Stage)<br><br>
    Random Forest achieved the best score on <strong>both</strong> metrics and was selected as the final model.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════
# TAB 3 — Feature Importance
# ════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="sec">🔍 What Drives the Predictions?</div>', unsafe_allow_html=True)
    st.caption("Higher % = more influential in the model's decisions")

    fi = {
        "Confederation strength vs era": 0.253,
        "Historical consistency":        0.123,
        "Total historical goals":        0.095,
        "Goals per match":               0.082,
        "Last 3 tournaments avg goals":  0.078,
        "Year":                          0.063,
        "Country (encoded)":             0.059,
        "Avg matches per tournament":    0.053,
        "Is host nation":                0.043,
        "Historical momentum":           0.039,
    }
    fi_df = pd.DataFrame({
        "Feature":    list(fi.keys()),
        "Importance": list(fi.values()),
        "Pct":        [f"{v:.1%}" for v in fi.values()]
    }).sort_values("Importance")

    fig4 = go.Figure(go.Bar(
        x=fi_df["Importance"],
        y=fi_df["Feature"],
        orientation="h",
        marker_color=[
            "#1a6b3c" if v > 0.15 else "#2d9e5f" if v > 0.08 else "#7DC8A0"
            for v in fi_df["Importance"]
        ],
        text=fi_df["Pct"],
        textposition="outside",
        textfont=dict(size=12, color="#111"),
    ))
    fig4.update_layout(
        height=420, plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Inter", size=12, color="#111"),
        xaxis=dict(showgrid=True, gridcolor="#EEE", tickformat=".0%",
                   tickfont=dict(color="#555")),
        yaxis=dict(tickfont=dict(size=12, color="#111")),
        margin=dict(l=10, r=80, t=10, b=10),
    )
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown('<div class="sec">📌 Key Insights</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div class="ibox"><strong>🥇 Confederation strength vs era (25.3%)</strong><br>How strong a team is relative to their era\'s competition — the most powerful predictor.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ibox"><strong>📈 Historical consistency (12.3%)</strong><br>Teams that consistently perform well across multiple tournaments are more predictable.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="ibox"><strong>⚽ Goals history (9.5% + 8.2%)</strong><br>Total historical goals and goals per match capture a team\'s long-term scoring ability.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ibox"><strong>🏠 Host nation effect (4.3%)</strong><br>Being the host has a measurable positive effect — home advantage is real even historically.</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.78rem;padding:16px 0'>"
    "Built for Zindi · World Cup 2026 Goal Prediction Challenge · Random Forest · scikit-learn"
    "</div>",
    unsafe_allow_html=True
)
