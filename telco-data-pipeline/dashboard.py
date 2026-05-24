import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# =========================================================
# AUTO REFRESH
# =========================================================

st_autorefresh(interval=4000, key="live_refresh")

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Telecom Predictive AIOps",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* BACKGROUND */

.stApp{
    background:
    radial-gradient(circle at top left,#101c5a 0%,#030b2b 40%,#010615 100%);
    color:white;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background:#071038;
    border-right:1px solid rgba(255,255,255,0.06);
    width:250px !important;
}

.sidebar-title{
    font-size:18px;
    font-weight:700;
    color:white;
    margin-top:25px;
    margin-bottom:28px;
}

.nav-item{
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    padding:14px;
    border-radius:18px;
    margin-bottom:12px;
    font-size:14px;
    font-weight:600;
    color:white;
}

.nav-item:hover{
    background:rgba(255,255,255,0.06);
    transition:0.3s;
}

.footer-box{
    background:linear-gradient(90deg,#0d5037,#0f3d2e);
    border-radius:18px;
    padding:18px;
    font-size:16px;
    font-weight:700;
    color:#65ff9d;
    margin-top:30px;
    text-align:center;
}

/* HEADER */

.main-title{
    font-size:42px;
    font-weight:900;
    line-height:1.1;
    color:white;
    margin-top:10px;
}

.sub-title{
    font-size:14px;
    color:#9ca3af;
    margin-top:8px;
    margin-bottom:25px;
}

/* AI INSIGHT */

.ai-box{
    background:linear-gradient(90deg,#34156e,#13245b);
    border:1px solid #8b5cf6;
    border-radius:22px;
    padding:22px;
    color:white;
    font-size:15px;
    margin-bottom:22px;
    box-shadow:0 0 20px rgba(139,92,246,0.18);
}

/* METRIC CARDS */

.metric-card{
    background:linear-gradient(180deg,#06133f,#061131);
    border-radius:22px;
    padding:20px;
    height:180px;
    overflow:hidden;
    margin-bottom:20px;
}

.metric-card-purple{
    border:1px solid rgba(168,85,247,0.45);
    box-shadow:0 0 20px rgba(168,85,247,0.15);
}

.metric-card-red{
    border:1px solid rgba(239,68,68,0.45);
    box-shadow:0 0 20px rgba(239,68,68,0.15);
}

.metric-card-orange{
    border:1px solid rgba(245,158,11,0.45);
    box-shadow:0 0 20px rgba(245,158,11,0.15);
}

.metric-card-blue{
    border:1px solid rgba(6,182,212,0.45);
    box-shadow:0 0 20px rgba(6,182,212,0.15);
}

.icon-circle{
    width:55px;
    height:55px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
}

.metric-title{
    font-size:13px;
    font-weight:600;
    margin-top:12px;
}

.metric-value{
    font-size:38px;
    font-weight:800;
    margin-top:8px;
}

.metric-sub{
    color:#9ca3af;
    font-size:12px;
    margin-top:4px;
}

/* CHART CARDS */

.chart-card{
    background:linear-gradient(180deg,#07143f,#071132);
    border-radius:22px;
    padding:14px;
    border:1px solid rgba(255,255,255,0.05);
    margin-top:10px;
}

.chart-title{
    font-size:16px;
    font-weight:700;
    margin-bottom:10px;
}

/* SMALL CARDS */

.small-card{
    background:linear-gradient(180deg,#07143f,#071132);
    border-radius:22px;
    padding:14px;
    border:1px solid rgba(255,255,255,0.05);
    margin-top:15px;
}

.card-title{
    font-size:15px;
    font-weight:700;
    margin-bottom:12px;
}

/* TABLE */

[data-testid="stDataFrame"]{
    border-radius:14px;
    overflow:hidden;
    border:1px solid rgba(255,255,255,0.08);
}

/* FOOTER */

.footer{
    margin-top:30px;
    padding:18px;
    border-radius:18px;
    background:linear-gradient(90deg,#0f5132,#063a26);
    color:#7CFFB2;
    text-align:center;
    font-size:14px;
    font-weight:600;
    border:1px solid rgba(124,255,178,0.2);
}

/* REMOVE STREAMLIT */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-title">
    📡 Telecom AIOps
    </div>
    """, unsafe_allow_html=True)

    nav_items = [
        "🏠 Overview Dashboard",
        "📊 KPI Intelligence",
        "🚨 Incident Analytics",
        "📈 Risk Prediction",
        "🔮 Predictive Forecasting",
        "🛠 Self-Healing Automation",
        "📑 Executive Monitoring"
    ]

    for item in nav_items:
        st.markdown(
            f'<div class="nav-item">{item}</div>',
            unsafe_allow_html=True
        )

    st.markdown("""
    <div class="footer-box">
    🟢 Platform Operational
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="main-title">
Telecom Predictive AIOps Platform
</div>

<div class="sub-title">
Enterprise Telecom Monitoring & Incident Intelligence Dashboard
</div>
""", unsafe_allow_html=True)

# =========================================================
# AI INSIGHT
# =========================================================

st.markdown("""
<div class="ai-box">
🧠 <b>AI Insight:</b>
Congestion escalation detected in Cell_Beta_002.
Traffic redistribution recommendation generated successfully.
</div>
""", unsafe_allow_html=True)

# =========================================================
# METRIC CARDS
# =========================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card metric-card-purple">
    <div class="icon-circle" style="background:rgba(168,85,247,0.18);">🔔</div>
    <div class="metric-title">Total Alerts</div>
    <div class="metric-value">15</div>
    <div class="metric-sub">All active alerts</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card metric-card-red">
    <div class="icon-circle" style="background:rgba(239,68,68,0.18);">🔥</div>
    <div class="metric-title">Critical Alerts</div>
    <div class="metric-value">4</div>
    <div class="metric-sub">Requires immediate attention</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card metric-card-orange">
    <div class="icon-circle" style="background:rgba(245,158,11,0.18);">⚠️</div>
    <div class="metric-title">High Risk Alerts</div>
    <div class="metric-value">5</div>
    <div class="metric-sub">High priority alerts</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card metric-card-blue">
    <div class="icon-circle" style="background:rgba(6,182,212,0.18);">📉</div>
    <div class="metric-title">KPI Anomalies</div>
    <div class="metric-value">1</div>
    <div class="metric-sub">Anomalies detected</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# REAL TIME MONITORING
# =========================================================

st.markdown("""
<div class="small-card">
<div class="card-title">
📡 Real-Time Monitoring Status
</div>
""", unsafe_allow_html=True)

monitor_df = pd.DataFrame({
    "Tower":["Tower_A12","Tower_B07","Tower_C21","Tower_D18"],
    "Latency(ms)":[12,18,10,14],
    "Packet Loss":["0.2%","0.5%","0.1%","0.3%"],
    "Network Status":["Stable","Moderate","Stable","Stable"]
})

st.dataframe(
    monitor_df,
    use_container_width=True,
    height=220
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CHARTS
# =========================================================

left,right = st.columns(2)

with left:

    st.markdown("""
    <div class="chart-card">
    <div class="chart-title">
    📈 Risk Trend (Last 7 Days)
    </div>
    """, unsafe_allow_html=True)

    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(
        x=["10AM","11AM","12PM","1PM","2PM","3PM","4PM"],
        y=[10,14,12,17,19,15,22],
        mode="lines+markers",
        fill="tozeroy",
        line=dict(color="#b15cff", width=4, shape="spline"),
        marker=dict(size=6,color="#d8b4fe"),
        fillcolor='rgba(177,92,255,0.25)'
    ))

    fig1.update_layout(
        paper_bgcolor="#071132",
        plot_bgcolor="#071132",
        height=300,
        margin=dict(l=10,r=10,t=10,b=10),
        xaxis=dict(showgrid=False,color="white"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.08)",color="white"),
        font=dict(color="white"),
        transition={'duration':1000}
    )

    st.plotly_chart(fig1,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="chart-card">
    <div class="chart-title">
    🚨 Priority Escalation Trend
    </div>
    """, unsafe_allow_html=True)

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=["P4","P3","P2","P1"],
        y=[1,3,6,9],
        mode="lines+markers",
        fill="tozeroy",
        line=dict(color="#4791ff", width=4, shape="spline"),
        marker=dict(size=6,color="#93c5fd"),
        fillcolor='rgba(71,145,255,0.25)'
    ))

    fig2.update_layout(
        paper_bgcolor="#071132",
        plot_bgcolor="#071132",
        height=300,
        margin=dict(l=10,r=10,t=10,b=10),
        xaxis=dict(showgrid=False,color="white"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.08)",color="white"),
        font=dict(color="white"),
        transition={'duration':1000}
    )

    st.plotly_chart(fig2,use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# LIVE TELECOM ALERTS
# =========================================================

st.markdown("""
<div class="small-card">
<div class="card-title">
🚨 Live Telecom Alerts
</div>
""", unsafe_allow_html=True)

live_alerts = pd.DataFrame({
    "Time":["10:42 AM","10:45 AM","10:48 AM","10:51 AM"],
    "Severity":["Critical","High","Medium","Critical"],
    "Incident":[
        "Fiber Link Failure",
        "Cell Congestion Spike",
        "VPN Tunnel Instability",
        "Power Supply Alert"
    ]
})

st.dataframe(
    live_alerts,
    use_container_width=True,
    height=220
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# KPI HEATMAP
# =========================================================

st.markdown("""
<div class="chart-card">
<div class="chart-title">
🔥 KPI Heat Map
</div>
""", unsafe_allow_html=True)

heatmap_fig = go.Figure(data=go.Heatmap(

    z=[
        [80,65,70,90],
        [60,55,75,95],
        [40,35,60,88]
    ],

    x=[
        "Latency",
        "Throughput",
        "PRB Usage",
        "Congestion"
    ],

    y=[
        "Cell_Alpha",
        "Cell_Beta",
        "Cell_Gamma"
    ],

    colorscale="Turbo"
))

heatmap_fig.update_layout(

    paper_bgcolor="#071132",
    plot_bgcolor="#071132",

    height=350,

    font=dict(color="white"),

    margin=dict(l=10,r=10,t=10,b=10)
)

st.plotly_chart(
    heatmap_fig,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TELECOM MAP
# =========================================================

st.markdown("""
<div class="chart-card">
<div class="chart-title">
🗺 Telecom Tower Map Visualization
</div>
""", unsafe_allow_html=True)

map_df = pd.DataFrame({
    "lat":[13.0827,13.0451,13.0674,13.0902],
    "lon":[80.2707,80.2496,80.2376,80.2788]
})

st.map(map_df)

st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TABLES
# =========================================================

t1,t2,t3 = st.columns(3)

with t1:

    st.markdown("""
    <div class="small-card">
    <div class="card-title">
    🧠 KPI Anomalies
    </div>
    """, unsafe_allow_html=True)

    anomaly_df = pd.DataFrame({
        "Object":["Cell_Alpha_001","Cell_Beta_002","Cell_Gamma_003"],
        "Status":["Normal","Anomaly Detected","Normal"]
    })

    st.dataframe(anomaly_df,use_container_width=True,height=220)

    st.markdown("</div>", unsafe_allow_html=True)

with t2:

    st.markdown("""
    <div class="small-card">
    <div class="card-title">
    🔮 Predictive Forecast
    </div>
    """, unsafe_allow_html=True)

    forecast_df = pd.DataFrame({
        "Object":["Cell_Alpha_001","Cell_Beta_002","Cell_Gamma_003"],
        "Forecast":[
            "Infrastructure stable",
            "Congestion escalation likely",
            "Infrastructure stable"
        ]
    })

    st.dataframe(forecast_df,use_container_width=True,height=220)

    st.markdown("</div>", unsafe_allow_html=True)

with t3:

    st.markdown("""
    <div class="small-card">
    <div class="card-title">
    🛠 Self-Healing
    </div>
    """, unsafe_allow_html=True)

    heal_df = pd.DataFrame({
        "Object":["Cell_Alpha_001","Cell_Beta_002","Cell_Gamma_003"],
        "Recommendation":[
            "No action required",
            "Traffic redistribution",
            "Infrastructure stable"
        ]
    })

    st.dataframe(heal_df,use_container_width=True,height=220)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
🟢 Telecom Predictive AIOps Platform •
AI Monitoring Active •
Real-Time Monitoring Enabled •
Data Pipeline Healthy
</div>
""", unsafe_allow_html=True)