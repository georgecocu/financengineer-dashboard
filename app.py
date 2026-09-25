import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Executive Triad Dashboard", page_icon="🏢", layout="wide")

# --- AUTHENTICATION MODULE ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# --- LOGOS HEADER (ACCA, CIA/IIA, ACFE/CFE) ---
def render_logos_header():
    """Renders logo badges for ACCA, IIA/CIA, and ACFE/CFE professional bodies."""
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; gap: 24px; margin-bottom: 20px; flex-wrap: wrap;">
            <!-- ACCA (FCCA) Logo Badge -->
            <div style="background: rgba(227, 24, 55, 0.06); border: 1px solid rgba(227, 24, 55, 0.3); border-radius: 10px; padding: 12px 22px; text-align: center; min-width: 170px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="font-weight: 900; font-size: 22px; color: #E31837; letter-spacing: 1.5px; font-family: sans-serif;">ACCA</div>
                <div style="font-size: 11px; font-weight: 600; color: #777777; margin-top: 2px;">Financial Results (FCCA)</div>
            </div>
            <!-- IIA / CIA Logo Badge -->
            <div style="background: rgba(0, 90, 156, 0.06); border: 1px solid rgba(0, 90, 156, 0.3); border-radius: 10px; padding: 12px 22px; text-align: center; min-width: 170px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="font-weight: 900; font-size: 22px; color: #005A9C; letter-spacing: 1.5px; font-family: sans-serif;">IIA / CIA</div>
                <div style="font-size: 11px; font-weight: 600; color: #777777; margin-top: 2px;">Internal Audit (CIA)</div>
            </div>
            <!-- ACFE / CFE Logo Badge -->
            <div style="background: rgba(0, 135, 90, 0.06); border: 1px solid rgba(0, 135, 90, 0.3); border-radius: 10px; padding: 12px 22px; text-align: center; min-width: 170px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="font-weight: 900; font-size: 22px; color: #00875A; letter-spacing: 1.5px; font-family: sans-serif;">ACFE / CFE</div>
                <div style="font-size: 11px; font-weight: 600; color: #777777; margin-top: 2px;">Fraud Stance (CFE)</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Render Professional Logos on Login Screen
        render_logos_header()
        
        st.title("🔒 Executive Portal Login")
        st.caption("Financengineer App — C-Suite Triad System")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Log In")
            
            if submit:
                # Demo Credentials
                if username == "trial" and password == "Trial2026":
                    st.session_state["authenticated"] = True
                    st.rerun()
                else:
                    st.error("Invalid credentials. Use demo / triad2026")

if not st.session_state["authenticated"]:
    render_login()
    st.stop()

# --- AUTHENTICATED DASHBOARD CONTENT ---
st.sidebar.write("👤 Logged in as: **Demo Executive**")
if st.sidebar.button("Log Out"):
    st.session_state["authenticated"] = False
    st.rerun()

# 1. Render Logos Above Dashboard Title
render_logos_header()

# 2. Main Dashboard Title
st.title("🏢 Executive Triad Dashboard")
st.caption("Integrated Financial, Internal Audit, and Fraud Intelligence System")

# Filtering Controls
col_ctrl1, col_ctrl2 = st.columns([1, 1])
with col_ctrl1:
    entity = st.selectbox("Entity / Region", ["Global Consolidated", "North America", "EMEA", "APAC"])
with col_ctrl2:
    period = st.selectbox("Reporting Period", ["Q2 2026", "Q1 2026", "FY 2025"])

st.markdown("---")

# --- TOP RIBBON: EXECUTIVE KPI BANNER ---
st.subheader("📊 Executive Health Check Banner")
ribbon_col1, ribbon_col2, ribbon_col3, ribbon_col4 = st.columns(4)

with ribbon_col1:
    st.metric(label="Operating Cash Flow", value="$4.2M", delta="-6.6% MoM", delta_color="inverse")
with ribbon_col2:
    st.metric(label="Net Profit Margin", value="18.5%", delta="+0.5% MoM")
with ribbon_col3:
    st.metric(label="Overdue Critical Audit Findings", value="2", delta="⚠️ +1 past target", delta_color="inverse")
with ribbon_col4:
    st.metric(label="Fraud Exposure Index", value="18 / 100", delta="Medium Risk Status", delta_color="off")

st.markdown("---")

# --- MAIN DASHBOARD GRID (3 VERTICALS) ---
col_fin, col_audit, col_fraud = st.columns(3)

# 1. FINANCIAL RESULTS (FCCA)
with col_fin:
    st.header("🟢 Financial Results")
    st.caption("FCCA Lens: Solvency, Profitability & Cash Flow")
    
    with st.container(border=True):
        st.subheader("P&L Performance")
        pnl_data = pd.DataFrame({
            "Metric": ["Revenue", "EBITDA", "Net Income"],
            "Actual ($M)": [14.2, 3.1, 2.6],
            "Target ($M)": [15.0, 3.2, 2.5]
        })
        st.dataframe(pnl_data, hide_index=True, use_container_width=True)

    with st.container(border=True):
        st.subheader("Liquidity & Cash Velocity")
        st.write("**Operating Cash:** $4.2M")
        st.write("**Cash Runway:** 14.2 Months")
        st.write("**Cash Conversion Cycle:** 42 Days")

    with st.container(border=True):
        st.subheader("Balance Sheet Health")
        st.write("**Current Ratio:** 1.8x")
        st.write("**Debt-to-Equity:** 0.45")
        st.write("**Bad Debt Provision:** 2.1% of AR")

# 2. INTERNAL AUDIT HEALTH (CIA)
with col_audit:
    st.header("🔵 Internal Audit Health")
    st.caption("CIA Lens: Risk Governance & Control Status")

    with st.container(border=True):
        st.subheader("Top Enterprise Risks")
        risk_df = pd.DataFrame({
            "Risk Area": ["Cybersecurity", "Supply Chain", "AML Compliance"],
            "Residual": ["High 🔴", "High 🔴", "Low 🟢"]
        })
        st.dataframe(risk_df, hide_index=True, use_container_width=True)

    with st.container(border=True):
        st.subheader("Control Effectiveness")
        control_chart = px.pie(
            names=["Effective", "Needs Improvement", "Deficient"],
            values=[85, 10, 5],
            color_discrete_sequence=["#2ecc71", "#f1c40f", "#e74c3c"],
            hole=0.4
        )
        control_chart.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)
        st.plotly_chart(control_chart, use_container_width=True)

    with st.container(border=True):
        st.subheader("Action Plan Tracking (MAPs)")
        st.write("**Open Issues:** 12 Total")
        st.error("**Overdue Critical:** 2 Issues")
        st.write("**Repeat Issue Index:** 0.0%")

# 3. FRAUD STANCE (CFE)
with col_fraud:
    st.header("🔴 Fraud Stance & Integrity")
    st.caption("CFE Lens: Anomaly Detection & Prevention")

    with st.container(border=True):
        st.subheader("Active Detection Flags")
        st.warning("⚠️ Vendor #402: Unverified Bank Detail Change")
        st.warning("⚠️ 18 Duplicate Invoice Flags ($42k Held)")

    with st.container(border=True):
        st.subheader("Whistleblower Hotline")
        st.write("**New Cases (Q2):** 4")
        st.write("**Under Investigation:** 2")
        st.write("**Substantiated:** 1")

    with st.container(border=True):
        st.subheader("Culture & Compliance")
        st.progress(0.94, text="Anti-Fraud Training Completion: 94%")
        st.progress(0.98, text="Conflict of Interest Completion: 98%")

st.markdown("---")

# TRIAD ALERT ENGINE
st.subheader("🚨 Triad Alert Engine")
with st.expander("⚠️ **CRITICAL CROSS-DOMAIN ALERT DETECTED**", expanded=True):
    st.error("""
    **Correlation Identified:**
    1. **Financial:** Unexpected 14% OpEx spike in Region B.
    2. **Internal Audit:** Failed control test — purchasing limits bypassed.
    3. **Fraud:** Vendor #801 shares bank details with HR Employee ID #4402.
    
    **Recommended Action:** Trigger immediate forensic hold on **$120,000 disbursement**.
    """)
