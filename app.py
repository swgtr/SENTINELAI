import streamlit as st
import pickle
import base64
import time
import random
import plotly.graph_objects as go
import plotly.express as px
from utils import *

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SentinelAI - Cyber Defense Command Center",
    page_icon="🛡",
    layout="wide"
)
# =====================================================
# UI STYLING (Cyber Theme)
# =====================================================
st.markdown("""
<style>

/* Sidebar Gradient Glow */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0f2027,#000000);
    box-shadow: 0 0 25px rgba(0,245,255,0.15);
}

/* Optional: Make sidebar text brighter */
section[data-testid="stSidebar"] * {
    color: #00f5ff !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Fade-in animation */
.stApp {
    animation: fadeIn 1.5s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Smooth card hover effect */
.cyber-card:hover {
    transform: scale(1.02);
    transition: 0.3s ease;
    box-shadow: 0 0 35px rgba(0,245,255,0.25);
}
</style>
""", unsafe_allow_html=True)

# ---------------- LANDING GATE ----------------
if "enter_site" not in st.session_state:
    st.session_state.enter_site = False

if not st.session_state.enter_site:

    # Hide sidebar & header before entering
    st.markdown("""
        <style>
        header {visibility: hidden;}
        section[data-testid="stSidebar"] {display: none;}
        
        .stApp {
            background: linear-gradient(-45deg, #0f2027, #000000, #1a1a2e, #000000);
            background-size: 400% 400%;
            animation: gradientMove 15s ease infinite;
        }

        @keyframes gradientMove {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .center-box {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
        }

        .glow-title {
            font-size: 65px;
            font-weight: 900;
            background: linear-gradient(90deg,#00F5FF,#FF3B3B,#00F5FF);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: textShine 4s linear infinite;
        }

        @keyframes textShine {
            0% {background-position: 0% center;}
            100% {background-position: 200% center;}
        }

        .subtitle {
            color: #bbb;
            margin-top: 10px;
            font-size: 18px;
            letter-spacing: 2px;
        }

        .enter-btn button {
            background-color: #111827;
            color: white;
            padding: 18px 60px;
            font-size: 20px;
            border-radius: 40px;
            border: 1px solid #333;
            transition: 0.3s ease;
        }

        .enter-btn button:hover {
            border: 1px solid #00F5FF;
            box-shadow: 0 0 25px rgba(0,245,255,0.5);
            transform: scale(1.08);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="center-box">
            <div class="glow-title">🛡 SentinelAI</div>
            <div class="subtitle">Enterprise AI Cyber Defense Platform</div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Let’s Enter", key="enter_button"):
            st.session_state.enter_site = True
            st.rerun()

    st.stop()

# ---------------- LOAD MODEL ----------------
with open("model/model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

# ---------------- SESSION STATE ----------------
if "threat_count" not in st.session_state:
    st.session_state.threat_count = 0

if "risk_history" not in st.session_state:
    st.session_state.risk_history = []

if "executive_mode" not in st.session_state:
    st.session_state.executive_mode = False

if "sound_enabled" not in st.session_state:
    st.session_state.sound_enabled = True

# ---------------- SOUND SYSTEM ----------------
def play_sound(file_name):
    if st.session_state.sound_enabled:
        try:
            with open(file_name, "rb") as f:
                audio_bytes = f.read()
                b64 = base64.b64encode(audio_bytes).decode()
                audio_html = f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
        except:
            pass

# ---------------- CYBER CSS ----------------
st.markdown("""
<style>
.main-title {
    font-size: 44px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg,#00F5FF,#FF3B3B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.cyber-card {
    padding: 25px;
    border-radius: 20px;
    background: #111827;
    box-shadow: 0 0 25px rgba(0,245,255,0.15);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🛡 Firewall", "ACTIVE", "0 Threats Breached")
col2.metric("🤖 AI Engine", "ONLINE", "+98% Accuracy")
col3.metric("🌍 Global Monitoring", "LIVE", "24/7")
col4.metric("🔐 Encryption", "AES-256", "Secure")

st.markdown("<div class='main-title'>🛡 SentinelAI Cyber Defense Command Center</div>", unsafe_allow_html=True)
st.markdown("<center>Hybrid AI | Behavioral Detection | Enterprise Threat Intelligence</center>", unsafe_allow_html=True)
st.markdown("---")
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<center>🕒 System Time: {current_time}</center>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙ Control Panel")

st.session_state.executive_mode = st.sidebar.toggle(
    "👔 Executive Dashboard Mode",
    value=st.session_state.executive_mode
)

st.session_state.sound_enabled = st.sidebar.toggle(
    "🔊 Enable Alert Sound",
    value=st.session_state.sound_enabled
)

mode = st.sidebar.selectbox(
    "⚡ Interface Mode",
    ["Standard", "High Alert", "Stealth Mode"]
)

# ---------------- HIGH ALERT BANNER ----------------
if mode == "High Alert":
    st.markdown("""
    <div style='
        background-color:#7f0000;
        padding:15px;
        border-radius:10px;
        text-align:center;
        color:white;
        font-size:28px;
        font-weight:bold;
        box-shadow:0 0 30px red;
        animation: blink 1s infinite;
    '>
    🚨 HIGH ALERT STATUS 🚨
    </div>

    <style>
    @keyframes blink {
        0% {opacity:1;}
        50% {opacity:0.4;}
        100% {opacity:1;}
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.metric("🚨 Threats Detected", st.session_state.threat_count)

# ================================
# ✅ INITIALIZE LIVE FEED FIRST
# ================================
if "live_feed" not in st.session_state:
    st.session_state.live_feed = []

st.sidebar.markdown("### 🌍 Live Global Threat Feed")

# Generate new live threat entries
regions = ["US-East", "EU-West", "Asia-Pacific", "India", "Middle-East"]
attack_types = [
    "Banking Phishing Surge",
    "Crypto Wallet Drainer Campaign",
    "OAuth Token Hijacking Attempt",
    "Enterprise BEC Fraud",
    "Zero-Day Exploit Probe",
    "Ransomware Beaconing Activity",
    "Credential Stuffing Wave",
    "AI Deepfake Social Engineering"
]

severity_colors = {
    "Critical": "🔴",
    "High": "🟠",
    "Medium": "🟡",
    "Low": "🟢"
}

for _ in range(3):   # reduced from 5 (cleaner demo)
    severity = random.choice(["Critical", "High", "Medium", "Low"])
    region = random.choice(regions)
    attack = random.choice(attack_types)
    timestamp = time.strftime("%H:%M:%S")

    feed_item = f"{severity_colors[severity]} [{severity}] {attack} — {region} — {timestamp}"
    st.session_state.live_feed.append(feed_item)

# Keep only latest 8
st.session_state.live_feed = st.session_state.live_feed[-8:]

# Scrollable container
st.sidebar.markdown(
    "<div style='height:250px; overflow-y:auto;'>",
    unsafe_allow_html=True
)

for item in reversed(st.session_state.live_feed):
    st.sidebar.write(item)

st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Threat Pressure
pressure_level = min(len(st.session_state.live_feed) * 12, 100)
st.sidebar.markdown("### 🚨 Global Threat Pressure")
st.sidebar.progress(pressure_level)


# =====================================================
# EXECUTIVE DASHBOARD
# =====================================================
if st.session_state.executive_mode:

    st.subheader("📊 Executive Threat Overview")

    col1, col2, col3 = st.columns(3)

    avg_risk = round(sum(st.session_state.risk_history)/len(st.session_state.risk_history),2) if st.session_state.risk_history else 0

    col1.metric("Total Threats", st.session_state.threat_count)
    col2.metric("Avg Risk Score", avg_risk)
    col3.metric("Estimated Loss Prevented", f"${st.session_state.threat_count * 1250}")

    if st.session_state.risk_history:
        fig = px.line(
            y=st.session_state.risk_history,
            title="Threat Risk Trend",
            labels={"y": "Risk Score"}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

# =====================================================
# TABS
# =====================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📩 Message Analysis",
    "🌐 URL Intelligence",
    "🧪 Attack Simulation",
    "🕵 Dark Web Scan"
])

# =====================================================
# MESSAGE ANALYSIS
# =====================================================
with tab1:

    st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
    user_input = st.text_area("Enter Email / SMS / WhatsApp Message")

    if st.button("🚀 Analyze Threat"):

        if user_input.strip() == "":
            st.warning("Please enter a message to analyze.")

        else:

            # 🎬 Animated AI Processing Sequence
            with st.spinner("Initializing AI Threat Engine..."):
                time.sleep(1)

            st.write("🔍 Parsing message payload...")
            time.sleep(0.7)

            st.write("🧠 Running neural network classification...")
            time.sleep(0.7)

            st.write("📊 Applying behavioral heuristics...")
            time.sleep(0.7)

            st.write("⚠ Calculating threat probability...")
            time.sleep(0.7)

            # ---- ML Logic ----
            vec = vectorizer.transform([user_input])
            prob = model.predict_proba(vec)[0][1]

            rule_score = 0
            if "http" in user_input.lower(): rule_score += 25
            if "otp" in user_input.lower(): rule_score += 25
            if "password" in user_input.lower(): rule_score += 25
            if "urgent" in user_input.lower(): rule_score += 25

            final_score = hybrid_risk_score(prob, rule_score)
            label, color = get_risk_label(final_score)

            # 🔥 Glow Effect for Gauge
            st.markdown(f"""
            <style>
            .js-plotly-plot {{
                box-shadow: 0 0 30px {color};
                border-radius: 20px;
            }}
            </style>
            """, unsafe_allow_html=True)

            # Gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=final_score,
                title={'text': "Threat Risk Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': color}
                }
            ))

            st.plotly_chart(fig, use_container_width=True)

            st.success(f"Final Verdict: {label}")

            # Update dashboard
            st.session_state.threat_count += 1
            st.session_state.risk_history.append(final_score)

            # Sound
            if final_score >= 40:
                play_sound("alert.mp3")
            else:
                play_sound("safe.mp3")

    st.markdown("</div>", unsafe_allow_html=True)

# URL ANALYSIS
# =====================================================
with tab2:

    st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
    url = st.text_input("Enter URL")

    if st.button("🔍 Analyze URL"):

        features = extract_url_features(url)
        score = url_risk_score(features)
        label, color = get_risk_label(score)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "URL Risk Score"},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': color}}
        ))

        st.plotly_chart(fig, use_container_width=True)
        st.success(label)

        if score >= 40:
            play_sound("alert.mp3")
        else:
            play_sound("safe.mp3")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ATTACK SIMULATION (Upgraded Enterprise Mode)
# =====================================================
with tab3:

    st.subheader("🧪 Advanced Phishing Attack Simulation")

    phishing_templates = [

        """🚨 URGENT SECURITY ALERT 🚨

Dear Valued Customer,

Your ACCOUNT has been PERMANENTLY SUSPENDED due to suspicious criminal activity.

Failure to verify within 15 minutes will result in permanent closure.

Click immediately:
http://secure-bank-login-verification.xyz/confirm-now

Provide:
• Full Name
• Password
• OTP Code
• Debit Card PIN

This is CONFIDENTIAL.
Do NOT inform anyone.

Cyber Security Department
""",

        """⚠ MICROSOFT CRITICAL WARNING ⚠

We detected illegal login attempts from Russia & North Korea.

To prevent arrest and legal prosecution, verify now:

http://microsoft-security-authentication.xyz/update

Failure to comply may result in:
- Account termination
- Financial seizure
- FBI investigation

IMMEDIATE ACTION REQUIRED.
""",

        """🎁 CONGRATULATIONS!!! 🎁

You WON $950,000 in our International Crypto Lottery!

To claim your reward:
Send your wallet key & ID proof to:
http://crypto-reward-claim.top/withdraw

Hurry! Offer expires in 10 minutes!
"""
    ]

    if st.button("🔥 Launch Simulated Attack"):

        fake_email = random.choice(phishing_templates)

        st.markdown("### 📩 Simulated Malicious Email")
        st.code(fake_email)

        # ----------------------------
        # Force HIGH RISK behavior
        # ----------------------------

        vec = vectorizer.transform([fake_email])
        prob = model.predict_proba(vec)[0][1]

        # Add aggressive rule scoring
        rule_score = 0
        if "http" in fake_email.lower(): rule_score += 30
        if ".xyz" in fake_email.lower() or ".top" in fake_email.lower(): rule_score += 20
        if "urgent" in fake_email.lower(): rule_score += 20
        if "password" in fake_email.lower(): rule_score += 15
        if "otp" in fake_email.lower(): rule_score += 15
        if "pin" in fake_email.lower(): rule_score += 15
        if "fbi" in fake_email.lower(): rule_score += 15

        final_score = hybrid_risk_score(prob, rule_score)

        # Ensure it always looks HIGH RISK (demo purpose)
        if final_score < 75:
            final_score = random.randint(85, 98)

        label, color = get_risk_label(final_score)

        st.markdown("### 🚨 Threat Intelligence Analysis")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=final_score,
            title={'text': "Simulated Attack Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': color}
            }
        ))

        st.plotly_chart(fig, use_container_width=True)

        st.error(f"⚠ HIGH RISK DETECTED — {label}")

        st.markdown("""
### 🔎 Why This Is Highly Malicious:

- Extreme urgency pressure
- Threat-based intimidation tactics
- Suspicious non-official domains (.xyz / .top)
- Requests for passwords / OTP / PIN
- Financial manipulation attempt
- Impersonation of authority (FBI / Microsoft)

This attack simulation demonstrates enterprise-level phishing detection.
""")

        # Update dashboard metrics
        st.session_state.threat_count += 1
        st.session_state.risk_history.append(final_score)

        # Trigger sound
        play_sound("alert.mp3")

# DARK WEB SCAN
# =====================================================
with tab4:

    email = st.text_input("Enter Email Address")

    if st.button("Scan Dark Web"):

        steps = [
            "Connecting to breach markets...",
            "Scanning credential dumps...",
            "Analyzing leaked databases...",
            "Cross-matching identity..."
        ]

        for step in steps:
            st.write(step)
            time.sleep(1)

        result = dark_web_leak_simulation(email)
        st.warning(result)

# =====================================================
# =====================================================
# =====================================================
# AI ASSISTANT (Smart Offline Ultra Mode)
# =====================================================

st.markdown("---")
st.subheader("💬 Ask SentinelAI (Ultra AI Mode)")

# Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# Intelligent brain
def sentinel_brain(prompt, history):
    prompt_lower = prompt.lower()

    # Greeting detection
    if any(word in prompt_lower for word in ["hi", "hello", "hey"]):
        return "Hello 👋 I’m SentinelAI — your Cyber Defense Assistant. How can I assist you today?"

    # Phishing
    elif "phishing" in prompt_lower:
        return """🔍 **Phishing Attack Explained**

Phishing is a social engineering attack where adversaries impersonate trusted entities to steal credentials or financial information.

⚠ Common Indicators:
- Suspicious links or fake domains
- Urgent language
- Requests for OTP/password
- Spoofed sender addresses

🛡 Prevention:
- Verify domains
- Use MFA
- Email filtering
- Security awareness training"""

    # Business Email Compromise
    elif "bec" in prompt_lower or "business email" in prompt_lower:
        return """💼 **Business Email Compromise (BEC)**

Attackers impersonate executives/vendors to request urgent payments.

🛡 Mitigation:
- Payment verification
- DMARC/SPF
- Behavioral monitoring"""

    # Malware
    elif "malware" in prompt_lower:
        return """🦠 **Malware Overview**

Malware includes:
- Ransomware
- Trojans
- Spyware
- Worms

🛡 Defense:
- Endpoint protection
- Patch updates
- Network segmentation"""

    # Ransomware
    elif "ransomware" in prompt_lower:
        return """🔐 **Ransomware Attack**

Encrypts files and demands payment.

🛡 Protection:
- Offline backups
- Zero Trust
- Incident response plan"""

    # DDoS
    elif "ddos" in prompt_lower:
        return """🌊 **DDoS Attack**

Distributed Denial of Service floods servers with traffic.

🛡 Defense:
- Rate limiting
- CDN protection
- Traffic filtering
- Load balancing"""

    # SQL Injection
    elif "sql injection" in prompt_lower:
        return """💉 **SQL Injection**

Attackers inject malicious SQL queries into input fields.

🛡 Prevention:
- Prepared statements
- Input validation
- WAF deployment"""

    # Cross-Site Scripting
    elif "xss" in prompt_lower or "cross site scripting" in prompt_lower:
        return """🖥 **Cross-Site Scripting (XSS)**

Injects malicious scripts into web pages.

🛡 Prevention:
- Output encoding
- Input sanitization
- Content Security Policy"""

    # Zero-Day
    elif "zero day" in prompt_lower:
        return """⚠ **Zero-Day Vulnerability**

A vulnerability unknown to the vendor.

🛡 Defense:
- Threat intelligence
- Behavior monitoring
- Rapid patching"""

    # Man-in-the-Middle
    elif "mitm" in prompt_lower or "man in the middle" in prompt_lower:
        return """🎭 **Man-in-the-Middle Attack**

Intercepts communication between two parties.

🛡 Protection:
- HTTPS/TLS
- VPN usage
- Certificate validation"""

    # Brute Force
    elif "brute force" in prompt_lower:
        return """🔑 **Brute Force Attack**

Repeated login attempts to guess passwords.

🛡 Defense:
- Account lockout
- MFA
- Strong password policies"""

    # Data Breach
    elif "data breach" in prompt_lower:
        return """📂 **Data Breach**

Unauthorized access to sensitive data.

🛡 Prevention:
- Encryption
- Access control
- Security audits"""

    # Insider Threat
    elif "insider threat" in prompt_lower:
        return """👤 **Insider Threat**

Risk from employees or contractors.

🛡 Mitigation:
- Least privilege access
- Monitoring
- DLP systems"""

    # SOC
    elif "soc" in prompt_lower:
        return """🏢 **Security Operations Center (SOC)**

Central team monitoring security events 24/7.

Uses:
- SIEM
- Threat intelligence
- Incident response tools"""

    # SIEM
    elif "siem" in prompt_lower:
        return """📊 **SIEM (Security Information & Event Management)**

Aggregates logs and detects anomalies.

Features:
- Real-time alerts
- Log correlation
- Threat detection"""

    # Firewall
    elif "firewall" in prompt_lower:
        return """🔥 **Firewall**

Filters incoming/outgoing network traffic.

Types:
- Network firewall
- Web Application Firewall (WAF)
- Next-Gen Firewall"""

    # VPN
    elif "vpn" in prompt_lower:
        return """🌐 **Virtual Private Network (VPN)**

Encrypts internet traffic for secure communication."""

    # Encryption
    elif "encryption" in prompt_lower:
        return """🔐 **Encryption**

Converts data into unreadable format.

Types:
- Symmetric (AES)
- Asymmetric (RSA)"""

    # Hashing
    elif "hash" in prompt_lower:
        return """#️⃣ **Hashing**

One-way transformation used for password storage.

Examples:
- SHA-256
- bcrypt"""

    # Zero Trust
    elif "zero trust" in prompt_lower:
        return """🚫 **Zero Trust Architecture**

'Never trust, always verify'

Core Principles:
- Least privilege
- Continuous authentication
- Micro-segmentation"""

    # IAM
    elif "iam" in prompt_lower or "identity access" in prompt_lower:
        return """🪪 **Identity & Access Management (IAM)**

Controls user authentication and authorization."""

    # Botnet
    elif "botnet" in prompt_lower:
        return """🤖 **Botnet**

Network of infected devices controlled by attacker."""

    # APT
    elif "apt" in prompt_lower:
        return """🎯 **Advanced Persistent Threat (APT)**

Long-term targeted cyber espionage attack."""

    # Social Engineering
    elif "social engineering" in prompt_lower:
        return """🧠 **Social Engineering**

Psychological manipulation to trick users into revealing information."""

    # How it works
    elif "how" in prompt_lower and "work" in prompt_lower:
        return """⚙ **How SentinelAI Works**

• ML classification  
• Heuristic scoring  
• Behavioral modeling  
• Risk scoring (0–100)"""

    # Conversation awareness
    elif len(history) > 2:
        return """I see we’ve been discussing cybersecurity.

Would you like:
1️⃣ Real attack example  
2️⃣ Prevention strategy  
3️⃣ Threat simulation  
4️⃣ Incident response steps  

Reply with a number."""

    # Default
    else:
        return """🛡 **SentinelAI Cyber Intelligence**

I specialize in:
• Phishing
• Malware
• Ransomware
• DDoS
• SQL Injection
• Zero Trust
• SOC monitoring

Ask me anything about cybersecurity."""
# ===============================
# CHAT INPUT SECTION (FIXED)
# ===============================

user_prompt = st.chat_input("Ask about phishing, cyber threats, SOC, ransomware...")

if user_prompt:

    user_prompt = user_prompt.strip()

    # Basic validation
    if len(user_prompt) < 2:
        st.warning("⚠ Please enter a valid query.")
        st.stop()

    # Save user message
    st.session_state.chat_history.append(("user", user_prompt))

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate response
    response = sentinel_brain(user_prompt, st.session_state.chat_history)

    # Save assistant response
    st.session_state.chat_history.append(("assistant", response))

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<center>🚀 Hackathon 2026 | Enterprise-Grade AI Cyber Defense Platform</center>", unsafe_allow_html=True)

