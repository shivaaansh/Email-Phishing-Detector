import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from scipy.sparse import hstack

data = pd.read_csv("phishing_dataset.csv")

tfidf = TfidfVectorizer(max_features=3000)
X_text = tfidf.fit_transform(data["email_text"])

X_url = data[
    ["url_length", "dot_count", "special_chars",
     "has_ip", "https", "subdomains", "digit_count"]
].values

X = hstack([X_text, X_url])
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "ml/phishing_model.pkl")
joblib.dump(tfidf, "ml/tfidf.pkl")
