# ==============================
# SMART FRAUD DETECTION - TRAIN MODEL
# ==============================

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.utils import resample

# ------------------------------
# LOAD DATASET
# ------------------------------

# Use full path OR keep spam.csv in same folder
DATA_PATH = r"E:\smart_fraud_detection\data\spam.csv"

if not os.path.exists(DATA_PATH):
    print("❌ Dataset not found! Check the path.")
    exit()

df = pd.read_csv(DATA_PATH, encoding="latin-1")

# ------------------------------
# FIX COLUMNS (for common spam datasets)
# ------------------------------

# If dataset has columns like v1, v2
if len(df.columns) >= 2:
    df = df.iloc[:, :2]
    df.columns = ["label", "text"]
else:
    print("❌ Dataset format incorrect.")
    exit()

# Convert label to numeric
df["label"] = df["label"].map({"ham": 0, "spam": 1})

print("\n📊 Original Class Distribution:")
print(df["label"].value_counts())

# ------------------------------
# BALANCE DATA (Very Important)
# ------------------------------

df_majority = df[df.label == 0]
df_minority = df[df.label == 1]

df_minority_upsampled = resample(
    df_minority,
    replace=True,
    n_samples=len(df_majority),
    random_state=42
)

df_balanced = pd.concat([df_majority, df_minority_upsampled])

print("\n📊 Balanced Class Distribution:")
print(df_balanced["label"].value_counts())

# ------------------------------
# SPLIT DATA
# ------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    df_balanced["text"],
    df_balanced["label"],
    test_size=0.2,
    random_state=42
)

# ------------------------------
# TF-IDF VECTORIZATION
# ------------------------------

vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ------------------------------
# TRAIN MODEL
# ------------------------------

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# ------------------------------
# EVALUATE MODEL
# ------------------------------

y_pred = model.predict(X_test_vec)

print("\n📈 Classification Report:\n")
print(classification_report(y_test, y_pred))

# ------------------------------
# SAVE MODEL + VECTORIZER
# ------------------------------

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\n✅ Model training complete!")
print("💾 model.pkl and vectorizer.pkl saved successfully.")
