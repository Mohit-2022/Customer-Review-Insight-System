import streamlit as st
import pickle
import pandas as pd
from text_preprocessing import clean_text
from aspect_detection import detect_aspects

# Load model & vectorizer
model = pickle.load(open('model.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

st.title("Customer Review Sentiment Analysis System")

menu = ["Single Review Analysis", "Bulk Review Analysis"]
choice = st.sidebar.selectbox("Select Mode", menu)

# ---------------- SINGLE REVIEW ---------------- #

if choice == "Single Review Analysis":

    st.subheader("Enter Customer Review")
    
    user_input = st.text_area("Type Review Here")
    
    if st.button("Analyze"):
        
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        
        prediction = model.predict(vector)[0]
        prob = model.predict_proba(vector)
        confidence = max(prob[0]) * 100
        
        if prediction == 1:
            st.success(f"Predicted Sentiment: Positive")
        else:
            st.error(f"Predicted Sentiment: Negative")
        
        st.write(f"Confidence Score: {confidence:.2f}%")
        
        if prediction == 0:
            issues = detect_aspects(user_input)
            if issues:
                st.write("Detected Issues:")
                for i in issues:
                    st.write(f"✔ {i}")
            else:
                st.write("No specific issue detected")

# ---------------- BULK REVIEW ---------------- #

elif choice == "Bulk Review Analysis":

    st.subheader("Upload CSV File with 'Review' Column")
    
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        
   df = pd.read_csv(uploaded_file)

# Remove hidden spaces from column names
df.columns = df.columns.str.strip()

# Convert all column names to lower case
df.columns = df.columns.str.lower()

if 'review' not in df.columns:
    st.error("Uploaded file must contain a column named 'Review'")
    st.write("Your columns are:", list(df.columns))
    st.stop()

df['Cleaned'] = df['review'].apply(clean_text)
vector = vectorizer.transform(df['Cleaned'])

df['Prediction'] = model.predict(vector)

total = len(df)
positive = sum(df['Prediction'] == 1)
negative = sum(df['Prediction'] == 0)

satisfaction = (positive/total) * 100

st.write(f"Total Reviews Analysed: {total}")
st.write(f"Positive Reviews: {positive}")
st.write(f"Negative Reviews: {negative}")
st.write(f"Customer Satisfaction Score: {satisfaction:.2f}%")

neg_df = df[df['Prediction'] == 0]

aspect_count = {}

for review in neg_df['review']:
    aspects = detect_aspects(review)
    for asp in aspects:
        aspect_count[asp] = aspect_count.get(asp,0)+1

st.subheader("Negative Issue Breakdown")

for asp in aspect_count:
    percent = (aspect_count[asp]/len(neg_df))*100
    st.write(f"{asp} Issues: {percent:.2f}%")
