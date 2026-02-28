import datetime
import re
from difflib import SequenceMatcher

# ---------------- URL FEATURE EXTRACTION ----------------
def extract_url_features(url):
    features = {}

    features["length"] = len(url)
    features["has_https"] = 1 if url.startswith("https") else 0
    features["num_dots"] = url.count(".")
    features["num_special_chars"] = len(re.findall(r"[@\-_%]", url))
    features["has_ip"] = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0

    return features


# ---------------- RULE-BASED URL RISK ----------------
def url_risk_score(features):
    score = 0

    if features["length"] > 50:
        score += 20

    if features["has_https"] == 0:
        score += 20

    if features["num_dots"] > 3:
        score += 20

    if features["num_special_chars"] > 2:
        score += 20

    if features["has_ip"] == 1:
        score += 20

    return min(score, 100)


# ---------------- HYBRID RISK ENGINE ----------------
def hybrid_risk_score(ml_probability, rule_score):
    return round((0.7 * (ml_probability * 100)) + (0.3 * rule_score), 2)


# ---------------- FAKE DOMAIN SIMILARITY DETECTOR ----------------
def domain_similarity_check(url):
    known_domains = ["amazon.com", "google.com", "paytm.com", "microsoft.com"]

    suspicious = []
    for domain in known_domains:
        similarity = SequenceMatcher(None, url.lower(), domain).ratio()
        if similarity > 0.75 and domain not in url.lower():
            suspicious.append((domain, round(similarity * 100, 2)))

    return suspicious


# ---------------- SOCIAL ENGINEERING DETECTOR ----------------
def detect_social_engineering(text):
    patterns = {
        "Fear": ["suspended", "blocked", "urgent", "immediately"],
        "Authority": ["ceo", "manager", "government", "bank"],
        "Reward Bait": ["win", "lottery", "prize", "free"],
        "Scarcity": ["limited", "last chance", "24 hours"]
    }

    detected = []

    for category, words in patterns.items():
        for word in words:
            if word in text.lower():
                detected.append(category)
                break

    return detected


# ---------------- BUSINESS EMAIL COMPROMISE DETECTOR ----------------
def detect_bec(text):
    if ("transfer" in text.lower() or "payment" in text.lower()) and \
       ("urgent" in text.lower() or "immediately" in text.lower()):
        return True
    return False


# ---------------- DARK WEB SIMULATION ----------------
def dark_web_leak_simulation(email):
    # Demo simulation logic
    if email.endswith("@gmail.com"):
        return "⚠ Email found in 2 past simulated breach databases."
    return "✅ No breach history detected (Simulated)"


# ---------------- DEEPFAKE / VOICE SCAM FLAG ----------------
def detect_deepfake_keywords(text):
    keywords = ["voice note", "ai generated", "deepfake", "recording"]
    return any(word in text.lower() for word in keywords)


# ---------------- LOGGING ----------------
def log_result(input_text, probability, risk_label):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()},{input_text},{probability},{risk_label}\n")
# ---------------- RISK LABEL ----------------
def get_risk_label(score):
    if score >= 75:
        return "HIGH RISK", "#FF3B3B"
    elif score >= 40:
        return "SUSPICIOUS", "#FFA500"
    else:
        return "SAFE", "#00FF9D"
