import joblib
from scipy.sparse import hstack
from ml.feature_extractor import extract_url_features

model = joblib.load("ml/phishing_model.pkl")
tfidf = joblib.load("ml/tfidf.pkl")

def predict_email(email_text, url):
    text_features = tfidf.transform([email_text])
    url_features = extract_url_features(url)

    combined_features = hstack([text_features, url_features])
    prediction = model.predict(combined_features)

    return prediction[0]  # 1 = phishing, 0 = safe
